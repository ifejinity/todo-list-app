from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("todos/create", views.create_todo, name="create_todo"),
    path("todos/delete/<uuid:id>", views.delete_todo, name="delete_todo"),
    path("todos/update/<uuid:id>", views.update_todo, name="update_todo"),
]