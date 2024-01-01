from django.urls import path

from schoolapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('newform', views.newform, name='newform'),
    path('message', views.message, name='message'),
    path('add_purpose', views.add_purpose, name='add_purpose'),
    path('logout',views.logout,name='logout'),
    path('load-courses/', views.load_courses, name='ajax_load_courses'),


]