from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),
    path('company/', views.company, name='company'),
]