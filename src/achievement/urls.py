from django.urls import path
from . import views

urlpatterns = [
    path('', views.achievement_view, name="achievement"),
    path('<int:achievement_id>', views.achievement, name="single_achievement"),
]