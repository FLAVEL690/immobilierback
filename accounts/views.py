from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm
from django.shortcuts import render, redirect
from .models import Shopper

# Create your views here.
class EmailLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'

User = get_user_model()
def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = Shopper.objects.create_user(email=email,username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        users = authenticate(password=password, username=email )
        if users:
            login(request,users)
            return redirect('index')


    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')






