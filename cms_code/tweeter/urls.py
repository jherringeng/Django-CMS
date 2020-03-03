from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    #path(r'^profile/(?P<user_name>\w+)$/', views.user_profile, name='user_profile'),
    re_path(r'^user-profile/(?P<user_name>)\w+$', views.user_profile, name='user-profile'),

    path('base', views.base, name='base'),

]
