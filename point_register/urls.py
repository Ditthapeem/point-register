from django.urls import path

from . import views

app_name = 'point_register'
urlpatterns = [
    path('', views.index, name='index'),
    path('bakery/', views.bakery_detail, name='bakery'),
    path('setbox/', views.setbox_detail, name='setbox'),
    path('register/', views.register, name="register"),
    path('update_point/', views.add_point, name="update_point"),
    path('สมัครสมาชิก/', views.user_register, name="user_register"), # link for user registration
    path('point/', views.user_point, name="user_point"),
    path('check point/', views.user_check_point, name="check_point"), # link for user check their point
    path('result check point', views.user_result_point, name="result_check_point"),
    
]