from django.urls import path

from . import views

urlpatterns = [
    path('users/register/', views.CreateUserView.as_view()),
    path('vehicles/', views.VehicleApiView.as_view())
]

