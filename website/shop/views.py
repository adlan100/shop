from django.shortcuts import render
from django.http import HttpResponse

def main_home(request):
    return render(request,'shop/home.html')

def main_shop(request):
    return render(request,'mag/shop.html')