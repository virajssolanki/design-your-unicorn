from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/<pk>', views.upload, name='upload'),
    path('<country_code>/<language_code>', views.index, name='upload'),
]