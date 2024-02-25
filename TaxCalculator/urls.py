from django.urls import path
from . import views

urlpatterns = [
    path("", views.Defaultpath, name='Defaultpath'),
    path('<str:price>', views.anyNumber, name='anyNumber'),
    path('taxrate/', views.taxrate, name='taxrate'),
]