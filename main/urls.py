from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('campaign/<campaign_id>/', views.campaign, name='campaign'),    
    path('upload/<frame_id>/<campaign_id>', views.upload, name='upload'),
    path('quiz/<campaign_id>', views.quiz, name='quiz'),
    path('<country_code>/<language_code>/', views.index, name='index'),
]