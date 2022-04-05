from django.urls import path
from .views import HomeView

app_name = "graphtask"

urlpatterns = [
    path('upload', HomeView, name="homepage"),
]
