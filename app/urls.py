from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('blog/', views.blog_posts, name='blog_posts'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
