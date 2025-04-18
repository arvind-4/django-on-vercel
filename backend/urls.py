"""backend URL Configuration for the project."""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path("about/", TemplateView.as_view(template_name="about.html")),
]
