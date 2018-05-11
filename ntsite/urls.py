from django.urls import path

from ntsite import views

urlpatterns = [
    path('', views.index, name='index'),
]