from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def landing_page(request):
    return render(request, 'core/landing_page.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    return render(request, 'core/login.html')

@csrf_protect
def do_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(1209600)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Email ou senha inválidos.')
            return redirect('core:login')
    return redirect('core:login')

def do_logout(request):
    logout(request)
    messages.info(request, 'Você foi desconectado.')
    return redirect('core:landing_page')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {'user': request.user})