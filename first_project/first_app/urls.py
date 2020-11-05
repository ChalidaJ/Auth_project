from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.create, name='register'),
    path('json/', views.random, name='json'),
    path('api/', views.Registerlist.as_view()),
]
