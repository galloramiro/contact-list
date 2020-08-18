from django_filters import FilterSet

from contacts.models import Contact


class ContactFilter(FilterSet):
    class Meta:
        model = Contact
        fields = ["name", "lastname", "email"]
        exclude = ["profile_picture"]