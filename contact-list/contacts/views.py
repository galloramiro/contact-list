from django.views.generic import ListView
from django_filters.views import FilterView
from rest_framework import viewsets

from rest_framework.filters import SearchFilter

from contacts.filters import ContactFilter
from contacts.models import Contact
from contacts.serializers import ContactModelSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer

    filter_backends = [SearchFilter]
    search_fields = ['=name', '=lastname', '=email']


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
