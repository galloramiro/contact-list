from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Contact model admin."""

    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('first_name', 'last_name', 'email')


admin.site.register(Contact, ContactAdmin)
