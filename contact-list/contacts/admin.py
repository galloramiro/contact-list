from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Contact model admin."""

    list_display = ('name', 'lastname', 'email', 'phone')
    list_filter = ('name', 'lastname', 'email')


admin.site.register(Contact, ContactAdmin)
