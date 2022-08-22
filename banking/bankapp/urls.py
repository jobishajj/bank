from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),

    path('login.html/', views.login, name='login'),
    path('register.html/', views.register, name='register'),
    path('sample.html/', views.sample, name='sample'),
    path('form.html/', views.form, name='form'),
    path('logout', views.logout, name='logout')
]
