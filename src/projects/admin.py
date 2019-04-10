from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator_name','is_published', 'list_date')
    list_display_links = ('title', 'creator_name')
    list_editable = ('is_published',)
    search_fields = ('title', 'list_date', 'creator_name')
    list_per_page = 25

admin.site.register(Project, ProjectsAdmin)
