from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("new/", views.book_create, name="book_create"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("<int:pk>/edit/", views.book_edit, name="book_edit"),
]
