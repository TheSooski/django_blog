from django.urls import path
from django import urls
from . import views

app_name = "sell"
urlpatterns = [
    #path("hompage/", views.article_list, name='list'),
    path('check/', views.sell_create, name='create'),
    #path('<slug:slug>/', views.sell_detail, name='detail')
]