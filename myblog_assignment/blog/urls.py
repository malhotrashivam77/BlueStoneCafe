from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('create/', views.create_blog, name='create_blog'),
]
