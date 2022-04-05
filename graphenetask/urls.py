from django.urls import path
from .views import HomeView
urlpatterns = [
    path('upload', HomeView, name="homepage"),
]
