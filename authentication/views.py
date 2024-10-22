from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import UserRegistrationForm


def register_view(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #* We could just save form since we used ModelForm but we need to hash the password first
            #form.save()

            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            # Hashing password
            user.set_password(password)
            form.save()
            messages.success(request, 'You Registered successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error Occured')
            return redirect('register')
    else:
        form = UserRegistrationForm()

    ctx = {'form': form}
    return render(request, 'authentication/register.html', context=ctx)



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You\'ve been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials!')
            return redirect('login')
            
    
    ctx = {}
    return render(request, 'authentication/login.html', context=ctx)


def logout_view(request):
    logout(request)
    messages.success(request, 'You\'ve been logged out successfully')
    return redirect('home')
