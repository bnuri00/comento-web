from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='new'),
    path('prod/', views.prodAll, name='prodAll'),
    path('<str:cate_name>/', views.prodList, name='prodList'),
    path('detail/<int:product_id>/', views.detail, name='detail'),  # ???
]
