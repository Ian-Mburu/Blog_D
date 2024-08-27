from django.shortcuts import render, redirect
from .forms import UserForm


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')
