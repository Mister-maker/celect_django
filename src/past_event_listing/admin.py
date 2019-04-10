from django.contrib import admin

from .models import Past_event

class PastEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'place', 'list_date')
    list_display_links = ('title', 'place')
    list_editable = ('is_published',)
    search_fields = ('title', 'list_date', 'place')
    list_per_page = 25


admin.site.register(Past_event, PastEventAdmin)

