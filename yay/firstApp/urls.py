from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("scale", views.scale, name="scale"),
    path("<str:name>", views.greet, name="greet")
]