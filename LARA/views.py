from django.shortcuts import render
from django.contrib import messages

from .models import Screen, Laptop
from .forms import AddScreen
#from django.http import HttpResponse

def lists(request):
    latest_laptop_list = Laptop.objects.order_by('-price')
    context = {'latest_laptop_list': latest_laptop_list}
    return render(request, 'laptop/lists.html', context)

def screen(request):

    screen_list = Screen.objects.all()
    
    if screen_list is None:
        messages.error(request, "No screen is found!")
        return render(request, 'screen/screen.html', {'screen_list': None})
    else:
        return render(request, 'screen/screen.html', {'screen_list': screen_list})

def addScreen(request):

    if request.method == 'POST':

        form = AddScreen(request.POST)
        if form.is_valid():
            screen = Screen(
                diagonal_size = form.cleaned_data['diagonal_size'],
                category = form.cleaned_data['cactegory'],
                resolution = form.cleaned_data['resolution'],
            )
            screen.save()
            messages.success(request, "The Screen has been successfully added!")
            return redirect('LARA:screen')
        else:
            messages.warning(request, "Sorry, the Screen can't be added!")
            return redirect('LARA:screen')

    else:
        form = AddScreen()
        return render(request, 'screen/add_screen.html', {'form': form})