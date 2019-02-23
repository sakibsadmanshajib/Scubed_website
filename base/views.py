from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test, login_required


def user_login(request):
    context = {}
    next = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('finance_management:account')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')
    
    else:
        return render(request, 'auth/login.html', context)


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('base:login')

def home(request):
    return render(request, 'home.html')

def comingSoon(request):
    if request.method == 'POST':
        form = ComingSoon(request.POST)
        if form.is_valid():
            subs = Subscriber(
                Name=form.cleaned_data['Name'],
                Email=form.cleaned_data['Email'],
                Timestamp=form.cleaned_data['Timestamp']
            )

            subs.save()
            messages.success(request, "Thank you.")
            return redirect('base:home')
        else:
            messages.warning(request, "Sorry something went wrong.")
            return redirect('base:home')
    else:
        form = ComingSoon()
        return redirect('base:home')

@login_required
def viewSubscribers(request):
    allSubscribers = Subscriber.objects.all()

    return render(request, 'base/subscriber/subscribers.html', {'subscribers' : allSubscribers})

