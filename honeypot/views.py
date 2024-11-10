from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def detail(request):
    return render(request, 'details.html')

def history(request):
    return render(request, 'history.html')

def transfer(request):
    if request.method == 'POST':
        return redirect('history')
    return render(request, 'transfer.html')

def profile(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'profile.html')