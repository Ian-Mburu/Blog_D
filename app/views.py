from django.shortcuts import render, redirect
from .forms import UserForm, BlogForm
from django.contrib import messages
from .models import RecipeDescription, Subscriber


def index(request):
    # Fetch all published posts
    posts = RecipeDescription.objects.filter(is_published=True)
    return render(request, 'index.html', {'posts': posts})


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
            return redirect('subscribe')
        else:
            messages.error(request, 'Please enter a valid email.')
    return render(request, 'subscribe.html')


# Blog Posts
def blog_posts(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.is_published = True
            form_instance.save()
            print("Recipe saved:", form_instance.recipeTitle)  # Debug print
            return redirect('index')  # Redirect to the index page to see the posts there
        else:
            print("Form errors:", form.errors)  # Debug print for form errors
    else:
        form = BlogForm()
    
    posts = RecipeDescription.objects.filter(is_published=True)
    return render(request, 'blog.html', {'posts': posts, 'form': form})  # Render to a separate blog page
