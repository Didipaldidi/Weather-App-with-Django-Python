from django.shortcuts import render, redirect
from .forms import RegistrationForm
from weather.views import index

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')  # Redirect to the 'city_list' URL pattern
    else:
        form = RegistrationForm()
        
    return render(request, 'register.html', {'form': form})