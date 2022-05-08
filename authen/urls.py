from django.urls import path, include
from .views import *

urlpatterns = [
    path("login", getLoginForm),
    path("register", getRegisterForm),
    path("activeRegister",register),
    path("activeLogin",loginAction),
    path("logout",logout_view),
    path("changePassword",getChangePassWordForm),
    path("changePasswordAction", change_password),
]
