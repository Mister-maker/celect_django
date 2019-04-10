from django.contrib import admin

from .models import Team 

class TeamAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Post','is_published')
    list_display_links = ('Name', 'Post')
    list_editable = ('is_published',)
    search_fields = ('Name', 'Post')
    list_per_page = 25

admin.site.register(Team, TeamAdmin)