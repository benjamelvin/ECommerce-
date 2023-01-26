from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('catagory/<str:name>', views.catagory),
    path('product/<int:id>', views.product),
    path('add-product/', views.add_product),
    path('shopping-cart', views.shopping),
    path('search', views.search1 ),
    path('search/<str:name>', views.search)

# ]
]