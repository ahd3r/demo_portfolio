from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('contact/', views.contact, name='contact'),
    path('write/', views.write_me, name='write_me'),
    path('add_a_message/', views.add_a_message, name='add_a_message'),
    path('for_me/', views.for_me, name='for_me'),
]
