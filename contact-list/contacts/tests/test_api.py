import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from contacts.models import Contact


@pytest.fixture
def contacts():
    contact1 = Contact(name="Ricardo", lastname="Example1", email="ricardo@example.com")
    contact1.save()
    contact2 = Contact(name="Max", lastname="Example1", email="max@example.com")
    contact2.save()
    contact3 = Contact(name="Anastasia", lastname="Example2", email="anastasia@example.com")
    contact3.save()
    contact4 = Contact(name="Anacleta", lastname="Example2", email="anacleta@example.com")
    contact4.save()


@pytest.mark.django_db
def test_list_contacts(contacts):
    client = APIClient()
    response = client.get(reverse("contacts:contact-list"))

    expected_respone = [
        dict(name="Ricardo", lastname="Example1", email="ricardo@example.com", phone=""),
        dict(name="Max", lastname="Example1", email="max@example.com", phone=""),
        dict(name="Anastasia", lastname="Example2", email="anastasia@example.com", phone=""),
        dict(name="Anacleta", lastname="Example2", email="anacleta@example.com", phone=""),
    ]

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_respone


@pytest.mark.django_db
def test_list_contacts_filtered_by_name(contacts):
    client = APIClient()
    params = dict(search="Ricardo")
    response = client.get(reverse("contacts:contact-list"), params)

    expected_respone = [
        dict(name="Ricardo", lastname="Example1", email="ricardo@example.com", phone=""),
    ]

    assert response.json() == expected_respone


@pytest.mark.django_db
def test_list_contacts_filtered_by_lastname(contacts):
    client = APIClient()
    params = dict(search="Example2")
    response = client.get(reverse("contacts:contact-list"), params)

    expected_respone = [
        dict(name="Anastasia", lastname="Example2", email="anastasia@example.com", phone=""),
        dict(name="Anacleta", lastname="Example2", email="anacleta@example.com", phone=""),
    ]

    assert response.json() == expected_respone


@pytest.mark.django_db
def test_list_contacts_filtered_by_email(contacts):
    client = APIClient()
    params = dict(search="max@example.com")
    response = client.get(reverse("contacts:contact-list"), params)

    expected_respone = [
        dict(name="Max", lastname="Example1", email="max@example.com", phone=""),
    ]

    assert response.json() == expected_respone
