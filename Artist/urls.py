from django.urls import path
from Artist import views

urlpatterns = [
    path('', views.landingpage, name="landing")
]
