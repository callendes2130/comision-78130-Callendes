from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/",  LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="accounts:login"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile_detail, name="profile_detail"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
]


#from accounts.views import *

#app_name = "accounts"
#LOGIN_REDIRECT_URL = reverse('accounts:login')

#urlpatterns = [
#    path("login/", LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
#    path("logout/", LogoutView.as_view(template_name = "accounts/logout.html"), name = "logout"),
#    path("register/", register, name="register"),
#    path("profile/", profile_detail, name="profile_detail"),    
#    path("profile/edit", profile_edit, name="profile_edit"),
#]

