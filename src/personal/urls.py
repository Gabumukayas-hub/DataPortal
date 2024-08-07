from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('farmer/', views.farmer_view, name = 'farmer_form'),
    #path('login/', views.login_user, name = 'login'),
    #path('logout/', views.logout_user, name = 'logout'),
]