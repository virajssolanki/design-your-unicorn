from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('s_upload/<pk>', views.simple_upload, name='upload'),
    path('upload/<pk>', views.upload, name='l_upload'),
]