from django.shortcuts import render

# Create your views here.
def viewShop(request):
    return render(request, 'shop/index.html')