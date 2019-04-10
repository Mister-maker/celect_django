from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'list_date', 'is_published', 'google_form_link')
    list_display_links = ('title', 'place')
    list_editable = ('is_published',)
    search_fields = ('title', 'list_date', 'place')
    list_per_page = 25


admin.site.register(Event, EventAdmin)
