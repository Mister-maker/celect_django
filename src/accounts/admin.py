from django.contrib import admin

from .models import RegistrationForm

class RegisterationFormAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'student_name', 'date_of_birth', 'email')
    list_display_links = ('roll_number', 'student_name')
    # list_filter = ('student_name',)
    search_fields = ('roll_number', 'student_name')
    list_per_page = 25


admin.site.register(RegistrationForm, RegisterationFormAdmin)
