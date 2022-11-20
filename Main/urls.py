from django import views
from django.urls import path
from .views import HomePageView, register
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(HomePageView.as_view()), name='Homepage'),
    path('accounts/register', register, name='register')
    
]
