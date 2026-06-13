from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .forms import RegisterForm


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"]
            )

            login(request, user)

            return redirect("property_list")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    error = None

    if request.method == "POST":

        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # Check if user entered an email
            user_obj = User.objects.get(email=username_or_email)
            username = user_obj.username
        except User.DoesNotExist:
            # Assume it's a username
            username = username_or_email

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("property_list")

        error = "Username/email atau password salah."

    return render(
        request,
        "accounts/login.html",
        {
            "error": error
        }
    )


def logout_view(request):

    logout(request)

    return redirect("login")