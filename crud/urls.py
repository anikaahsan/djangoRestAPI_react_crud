from django.urls import path
from . import views

urlpatterns=[
    path('',views.product, name='read'),
    path('detail/<int:pk>',views.product_detail,name='detail'),
    path('delete/<int:pk>',views.product_delete,name='delete'),
    path('update/<int:pk>',views.product_update,name='update')
 ]