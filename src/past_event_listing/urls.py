from django.urls import path
from . import views


urlpatterns = [
    path('', views.past_event_view_index, name="past_events"),
    path('<int:past_event_id>', views.past_event, name="past_event"),
]