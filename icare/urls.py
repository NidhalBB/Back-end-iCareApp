from django.urls import include, re_path
from icare import views
from .views import RegisterAPI,LoginAPI
from knox import views as knox_views

from django.conf import settings
from django.urls import path

urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^sport$',views.sportApi),
    re_path(r'^sport/([0-9]+)$',views.departmentApi),
    re_path('api/voice/',views.voiceApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),

    re_path(r'^employee/savefile',views.SaveFile),
    re_path('api/register/', RegisterAPI.as_view(), name='register'),
    re_path('api/login/', LoginAPI.as_view(), name='login'),
    re_path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    re_path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]