from django.urls import path

from ntsite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('systems/province', views.province_system, name='ProvinceSystem'),
]
