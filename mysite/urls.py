from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='new'),
    path('prod/', views.prodAll, name='prodAll'),
    path('<str:cate_name>/', views.prodList, name='prodList'),
    path('detail/<int:product_id>/', views.detail, name='detail'),  # ???
    path('comment/create/<int:product_id>/', views.comment_create, name='comment_create'),

    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
