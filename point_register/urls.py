from django.urls import path

from . import views

app_name = 'point_register'
urlpatterns = [
    path('', views.index, name='index'),
    path('bakery/', views.bakery_detail, name='bakery'),
    path('setbox/', views.setbox_deatail, name='setbox')
]