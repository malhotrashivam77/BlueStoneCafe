from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from .forms import BlogForm, BookingForm

def main_page(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def menu(request):
    return render(request, 'menu.html')

def booking(request):
    return render(request, 'booking.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_list')  # Redirect to the index page after login
            else:
                # Handle invalid login credentials
                return render(request, 'login.html', {'form': form, 'invalid_credentials': True})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login.html')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_data = form.cleaned_data
            return render(request, 'booking_data.html', {'booking_data': booking_data})
    else:
        form = BookingForm()
    return render(request, 'book_table.html', {'form': form})

def booking_data(request):
    return render(request, 'booking_data.html')