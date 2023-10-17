from django import forms
from guardian.shortcuts import get_objects_for_user

from apps.authentication.models import OnlineGroup
from apps.gallery.constants import ImageFormat
from apps.gallery.widgets import SingleImageInput


class OnlineGroupForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = get_objects_for_user(
            user=user, perms="authentication.change_onlinegroup", klass=OnlineGroup
        )
        instance: OnlineGroup = self.instance
        if instance.parent_group:
            queryset |= OnlineGroup.objects.filter(pk=instance.parent_group.id)

        self.fields["parent_group"].queryset = queryset

    class Meta:
        model = OnlineGroup
        fields = [
            "parent_group",
            "name_short",
            "name_long",
            "description_short",
            "description_long",
            "application_description",
            "email",
            "group_type",
            "roles",
            "admin_roles",
            "image",
        ]

        widgets = {
            "image": SingleImageInput(
                attrs={"id": "responsive-image-id", "preset": ImageFormat.GROUP}
            )
        }
