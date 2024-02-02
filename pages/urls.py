# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post_detail/", views.post_detail, name="post_detail"),
    # Add other paths as needed
]
