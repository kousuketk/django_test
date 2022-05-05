from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("members/", views.index, name="index"),
    path("members/add/", views.edit, name="add"),
    path("members/edit/<id>/", views.edit, name="edit"),
    path("members/delete/<id>/", views.delete, name="delete"),
    path("members/detail/<id>/", views.detail, name="detail"),
]
