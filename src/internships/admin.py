from django.contrib import admin

from .models import Internship

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'roll_number', 'list_date', 'year', 'is_published', 'company_name')
    list_display_links = ('full_name', 'roll_number')
    list_editable = ('is_published',)
    search_fields = ('full_name', 'list_date', 'year', 'company_name')
    list_per_page = 25

admin.site.register(Internship, InternshipAdmin)