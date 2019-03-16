from django.urls import path

from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('screen/', views.screen, name='screen'),
    path('screen/add/', views.addScreen, name='add_screen'),
]