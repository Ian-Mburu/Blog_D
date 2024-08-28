from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from .models import Subscriber


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


# Subscribe
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from the POST request
        if email:  # Check if the email was successfully retrieved
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, 'You are already subscribed.')
            else: 
                subscriber = Subscriber(email=email)
                subscriber.save()
                messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
        else:
            messages.error(request, 'Please enter a valid email.')
    # Render the form when the request method is GET or when there is an error
    return render(request, 'subscribe.html')