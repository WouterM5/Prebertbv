from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'pages/home.html')

def VeiligheidWelzijn(request):
    return render(request,'pages/VeiligheidWelzijn.html')

def juridische_kennisgeving(request):
    return render(request, 'pages/juridische_kennisgeving.html')