from rest_framework import serializers

from contacts.models import Contact


class ContactModelSerializer(serializers.ModelSerializer):
    """Contact model serializer."""

    class Meta:
        """Meta class."""

        model = Contact
        fields = (
            'name',
            'lastname',
            'email',
            'phone',
        )
