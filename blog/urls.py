from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<id_event>', views.every_event, name='every_event'),
]