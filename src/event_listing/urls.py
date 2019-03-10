from django.urls import path
from . import views


urlpatterns = [
    path('', views.event_view_index, name="events"),
    path('<int:event_id>', views.event, name="event"),
]