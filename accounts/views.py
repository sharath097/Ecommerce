from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.http import HttpResponse
from .signals import send_email_token

# Create your views here.
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.error(request, "Account not found.")
            return redirect("login")

        if not user_obj[0].Profile.is_email_verified:
            messages.error(request, "Your account is not verified.")
            return redirect("login")

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect("/")

        messages.warning(request, "Invalid credentials.")
        return redirect("login")

    return render(request, "accounts/login.html")


def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
            messages.warning(request, "An account with this email already exists.")
            return redirect("register")

        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "An email has been sent to your mail.")
        return redirect("register")

    return render(request, "accounts/register.html")

def activate_user(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return HttpResponse("Your email has been verified.")
    except Exception as e:
        return HttpResponse("Invalid email token.")