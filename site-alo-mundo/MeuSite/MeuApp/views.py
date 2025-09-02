from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'MeuApp/home.html')

def segundaPagina(request):
    return render(request, 'MeuApp/segundaPagina.html')
# Create your views here.
