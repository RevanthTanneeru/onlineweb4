from datetime import datetime, timedelta, timezone

from django.test import TestCase
from django.urls import reverse
from django_dynamic_fixture import G
from rest_framework import status

from apps.companyprofile.models import Company
from apps.online_oidc_provider.test import OIDCTestCase

from .models import CareerOpportunity


class CareerOpportunityURLTestCase(TestCase):
    def test_careeropportunity_index(self):
        url = reverse("careeropportunity_index")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_careeropportunity_detail(self):
        past = datetime(2000, 1, 1, 1, 0, 0, 0, timezone.utc)
        future = datetime.now(timezone.utc) + timedelta(days=1)
        careeropportunity = G(CareerOpportunity, start=past, end=future)

        url = reverse("careeropportunity_details", args=(careeropportunity.id,))

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CompanyAPITestCase(OIDCTestCase):
    basename = "careeropportunity"

    def setUp(self):
        self.company: Company = G(Company, name="online")
        self.past = datetime.now(timezone.utc) - timedelta(days=7)
        self.future = datetime.now(timezone.utc) + timedelta(days=7)
        self.opportunity: CareerOpportunity = G(
            CareerOpportunity, start=self.past, end=self.future, company=self.company
        )

    def test_careeropportunity_api_returns_200_ok(self):
        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_can_get_careeropportunity_by_id(self):
        response = self.client.get(self.get_detail_url(self.opportunity.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("title"), self.opportunity.title)

    def test_client_can_filter_careeropportunity_by_name(self):
        other_company: Company = G(Company, name="evilcorp")
        other_opportunity: CareerOpportunity = G(
            CareerOpportunity, start=self.past, end=self.future, company=other_company
        )

        response = self.client.get(f"{self.get_list_url()}?company={self.company.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        opportunity_titles = list(
            map(
                lambda opportunity: opportunity.get("title"),
                response.json().get("results"),
            )
        )

        self.assertIn(self.opportunity.title, opportunity_titles)
        self.assertNotIn(other_opportunity.title, opportunity_titles)
