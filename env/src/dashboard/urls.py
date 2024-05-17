from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.testHello), # Test URL
    path('data/', views.data_list), # Data URL
]
