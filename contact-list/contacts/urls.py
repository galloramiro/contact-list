from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet, ContactListView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', ContactListView.as_view(), name='contacts-list'),
    path('api/', include(router.urls)),
]