from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('s_upload/<pk>', views.simple_upload, name='upload'),
    path('l_upload/<pk>', views.l_upload, name='l_upload'),
]