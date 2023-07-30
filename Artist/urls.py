from django.urls import path
from Artist import views

urlpatterns = [
    path('', views.landingpage, name="landing"),
    path('login/', views.loginpage, name="login"),
    path('profile/', views.profilepage, name="profile")
]
