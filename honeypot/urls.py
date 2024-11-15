from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('history/',views.history, name='history'),
    path('detail/',views.detail, name='detail'),
    path('transfer/',views.transfer, name='transfer'),
    path('profile/',views.profile, name='profile'),
]