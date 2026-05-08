from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.login_page, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('do-login/', views.do_login, name='do_login'),
    path('logout/', views.do_logout, name='logout'),
]