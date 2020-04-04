from django.shortcuts import render, redirect
from appleStore.models import Product
from django.contrib import messages


# Create your views here.
def showIndex(request):
    return render(request, 'index.html', context={'procut':Product.objects.all()})


def saveProduct(request):
    pn = request.POST.get('name')
    pp = request.POST.get('price')
    pq = request.POST.get('quantity')
    pi = request.FILES['img']
    Product(name=pn, price=pp, quantity=pq, image=pi).save()
    messages.success(request, 'Product Successfully Saved!! ')
    return redirect('main')