from django.contrib import admin

from .models import Achievement

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('creator_name', 'title', 'list_date', 'is_published', 'project_link')
    list_display_links = ('title', 'creator_name')
    list_editable = ('is_published',)
    search_fields = ('title', 'creator_name')
    list_per_page = 25

admin.site.register(Achievement, AchievementAdmin)
