from django.shortcuts import render, redirect
from .forms import UserForm, BlogForm
from django.contrib import messages
from .models import RecipeDescription, Subscriber

from django.core.mail import send_mail


def index(request):
    # Fetch all published posts
    return render(request, 'index.html')
from django.shortcuts import render

def blog(request):
    # Your logic here
    return render(request, 'blog_form.html', {})




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
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, 'You are already subscribed.')
            else: 
                subscriber = Subscriber(email=email)
                subscriber.save()
                messages.success(request, 'Thank you for subscribing!')

                # send a confirmation email
        else:
            messages.error(request, 'Please enter a valid email.')
    return render(request, 'subscribe.html')


# Blog Posts
def blog_posts(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after successful submission
        else:
            print("Form errors:", form.errors)  # Debugging line
    else:
        form = BlogForm()

    posts = RecipeDescription.objects.filter(is_published=True)
    return render(request, 'blog_form.html', { 'form': form})




# 404 Error
def error_404(request, exception):
    return render(request, '404.html')