from django.urls import path
from . import views

urlpatterns = [
    path('main_page', views.main_page, name='main_page'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    # path('blogs/', views.blog_list, name='blog_list'),
    # path('create/', views.create_blog, name='create_blog'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('booking-data/', views.booking_data, name='booking_data'),
]
