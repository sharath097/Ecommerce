from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("activate/<email_token>", views.activate_user, name="activate_user")
]