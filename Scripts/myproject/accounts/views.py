from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'accounts/login.html')

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Forgot Password View
def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        # Send reset password email (you'll need to set up an email backend)
        send_mail(
            'Password Reset Instructions',
            'Here is the link to reset your password...',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return render(request, 'accounts/forgot_password.html', {'message': 'Password reset link sent to your email'})
    return render(request, 'accounts/forgot_password.html')

# Change Password View
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})

# Profile View
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

