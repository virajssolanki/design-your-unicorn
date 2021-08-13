from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/<pk>', views.simple_upload, name='upload'),
]