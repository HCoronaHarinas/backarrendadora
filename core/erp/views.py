from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from core.erp.models import Category, Product


def myfirstview(request):
    data = {
        'name': 'Hector',
        'categories' : Category.objects.all()
    }
    return render(request, 'login.html', data)


def mysecondview(request):
    data = {
        'name': 'Hector',
        'productos' : Product.objects.all()
    }
    return render(request, 'propietarios.html', data)