
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
]
