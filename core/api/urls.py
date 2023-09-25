from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('productlist/',productList,name='productList'),
    path('productdetail/<str:pk>/',productDetail,name='productDetail'),
    path('productcreate/',productCreate,name='productCreate'),
    path('productupdate/<str:pk>/',productUpdate,name='productUpdate'),
    path('productdelete/<str:pk>/',productDelete,name='productDelete'),
]
