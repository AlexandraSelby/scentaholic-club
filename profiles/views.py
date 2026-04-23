from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import SignUpForm

@user_passes_test(lambda user: not user.is_authenticated, login_url="/")
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect("login")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})