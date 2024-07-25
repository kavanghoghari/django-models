from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product, CartOrder, CartOrderItem, Category, Vendor, ProductImage, Wishlist

# Create your views here.
#def index(request):
 #   return HttpResponce("welcome to my shop")
def index(request):
    #return HttpResponse("<h1>contact page</h1>")
    return render(request, 'core/index.html')
def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'core/product.html', {'products': products})


def home(request):
    photo_data = {
        'photo_1': 'https://picsum.photos/seed/1/300/200',
        'photo_2': 'https://picsum.photos/seed/2/300/400',
        'photo_3': 'https://picsum.photos/seed/3/300/300',
        'photo_4': 'https://picsum.photos/seed/4/300/300',
        'photo_5': 'https://picsum.photos/seed/5/300/300',
        'photo_6': 'https://picsum.photos/seed/6/300/300',
        'photo_7': 'https://picsum.photos/seed/7/300/400',
        'photo_8': 'https://picsum.photos/seed/8/300/300',
        'photo_9': 'https://picsum.photos/seed/9/300/200',
        'photo_10': 'https://picsum.photos/seed/10/300/100',
        'photo_11': 'https://picsum.photos/seed/11/300/400',
        'photo_12': 'https://picsum.photos/seed/12/300/400',
    }
    return render(request, 'home.html', photo_data)
from django.shortcuts import render

def index(request):
    products = Product.objects.filter(product_status="published", featured=True)
    context = {
       "products": products
    }
    return render(request, 'core/index.html', context)  # Ensure correct indentation

def category_list_view(request):
        categories = Category.objects.all()
        context = {
        
          "categories":categories
        }
        return render(request, 'core/category-list.html', context)
