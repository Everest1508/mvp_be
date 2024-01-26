# yourapp/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('users/',Users.as_view(),name = 'users'),
     path('colleges/', CollegeListCreateView.as_view(), name='college-list-create'),
    path('games/', GamesListCreateView.as_view(), name='games-list-create'),
    path("verify/", VerifyOTPView.as_view(), name="")
]
