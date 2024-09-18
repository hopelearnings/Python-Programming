from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("hope", views.hope, name="Engineer"),
    path("<str:name>", views.greet, name="greet"),
]