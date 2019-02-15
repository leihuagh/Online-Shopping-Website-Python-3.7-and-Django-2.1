from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('info/', views.about_detail, name='about_detail'),
    ]
   