from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("books/", views.books_list, name='list'),
    path("create/", views.books_create, name='create'),
    path('<slug:slug>/', views.books_detail, name='detail')
]