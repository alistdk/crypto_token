from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "crypto_app/index.html")

def blog(request):
    return render(request, "crypto_app/blog.html")

def checkout(request):
    return render(request, "crypto_app/checkout.html")

def contact(request):
    return render(request, "crypto_app/contact.html")

def regular_page(request):
    return render(request, "crypto_app/regular-page.html")

def shop(request):
    return render(request, "crypto_app/shop.html")

def single_b(request):
    return render(request, "crypto_app/single-blog.html")

def single_p(request):
    return render(request, "crypto_app/single-product-details.html")

def login_p(request):
    return render(request, "crypto_app/login-metamask.html")