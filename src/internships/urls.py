from django.urls import path
from . import views

urlpatterns = [
    path('', views.internships_view, name="internships")
]