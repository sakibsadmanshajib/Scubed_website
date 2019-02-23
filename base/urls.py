from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('subscribers/', views.viewSubscribers, name='viewSubscribers'),
    path('comingsoon/', views.comingSoon, name='comingSoon'),
]