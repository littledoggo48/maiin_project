from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def registration(request):
    """ Display registration site"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # check the password
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                try:
                    user = User.objects.create_user(
                        username=username, 
                        password=password, 
                        email=email) 
                        
                    user.save()
                    # return a message
                    messages.success(request, 'registration was a success')
                    return redirect('app_member:sign_in')
                    
                except Exception as e:
                    messages.error(request, f'An error occurred: {e}')
                    
            else:
                messages.error(request, 'Username already exist')
      
    else:
        messages.error(request, 'Password do not much')

    return render(request, 'account/register.html')


def login_view(request):
    """ login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        # check if the user exist

        if user is not None:
            login(request, user)
            messages.success(request, 'welcome back')
            return redirect('app_main:home')
        
        else:
            messages.error(request, 'invalid credentials')
    return render(request, 'account/login.html')