from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='new'),
    path('<int:content_id>/', views.detail, name='detail'),
]
