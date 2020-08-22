from django.shortcuts import render
from .models import Product

# Create your views here.
def test(request):
    product = Product.objects.all()

    return render(request, 'test.html', {'product': product})

def product(request,pk):
    product_view = Product.objects.filter(id=pk)
    return render(request, 'product_view.html', {'product_view': product_view})



def base(request):
    return render(request, 'base.html')



def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})



def about(request):
    return render(request, 'Shop/about.html')


def contact(request):
    return render(request, 'Shop/contact.html')

def tracker(request):
    return render(request, 'Shop/index.html')

def search(request):
    pass



def checkout(request):
    pass

