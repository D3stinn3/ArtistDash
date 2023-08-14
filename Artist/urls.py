from django.urls import path
from Artist import views

urlpatterns = [
    path('', views.landingpage, name="landing"),
    path('login/', views.loginpage, name="login"),
    path('signin/', views.signuppage, name="signin"),
    path('signout/', views.signoutpage, name="signout"),
    path('profile/', views.profilepage, name="profile"),
    path('active/', views.activetasks, name="active"),
    path('pending/', views.pendingtasks, name="pending"),
]
