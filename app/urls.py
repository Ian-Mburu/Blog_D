from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blog/', views.blog, name='blog'),
    path('success/', views.success, name='success'),
]