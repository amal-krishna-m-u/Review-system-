from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == 'POST':
        # Get form data
        names = request.POST['name']
        email = request.POST['email']
        password2 = request.POST['password2']
        dob = request.POST['dob']
        hashedpswd = md5(password2)

        # Check if email is reserved
        if email == 'admin@gamil.com':
            messages.error(request, 'Reserved email')
            return redirect('register')

        # Check if account already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Account already exists')
            return redirect('register')

        # Create new user
        user = User.objects.create(
            user_name=names,
            dob=dob,
            password2=hashedpswd,
            email=email
        )
        user.save()

        # Set session variable and redirect to interest view
        request.session['login_user'] = names
        return redirect('interest')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('register')
