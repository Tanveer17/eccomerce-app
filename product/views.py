from django.shortcuts import render
from django.http.response import HttpResponse,Http404
from django.template import loader,Context
from .models import Product,Company
import math
# Create your views here.

def home(request):
    if not request.session.get('cart'):
        cart = []
        request.session['cart'] = cart
    slider_products = get_slider_products()
    latest_products = get_latest_products()
    cart = filter_cart(request)


    return render(request,
            'product/index.html',
            {'slider_products':slider_products,
                'latest_products':latest_products,
                'brand_list':Company.objects.all(),
                'cart':cart})
    pass

def get_slider_products():
    count = 0
    slider_products = []
    for item in Product.objects.all():
        if count < 4:
            slider_products.append(item)
        else:
            break
        count += 1
    return slider_products

def get_latest_products():
    count = 0
    latest_products = []
    for item in Product.objects.all():
        if count < 10:
            latest_products.append(item)
        else:
            break
        count += 1
    return latest_products


            
def shop(request,page_number):
    cart = filter_cart(request)
    pages = math.ceil(Product.objects.count()/12)
    if page_number > pages:
        raise Http404
    pages_dict = get_pages_dict(pages)
    items = get_from(Product.objects.all(),pages_dict[page_number])
    
    return render(request,
            'product/shop.html',
            {'products':items,
                'number_of_pages':pages,
                'cart':cart})
    pass

def single_product(request,slug):
    product = Product.objects.get(slug__iexact=slug)
    related_products = get_related_products(product)
    cart = filter_cart(request)
    return render(request,
            'product/single-product.html',
            {'related_products':related_products,
                'product':product,
                'cart':cart})

def get_from(items,frm):
    count = 1
    result = []
    
    for item in items:
        if count >= frm and len(result) < 12:
            result.append(item)
        
        count += 1
            
    return result

def get_pages_dict(pages):
    page_number = 1
    from_number_of_items = 1
    pages_dict = {}
    while page_number <= pages:
         pages_dict[page_number] = from_number_of_items
         page_number +=1
         from_number_of_items +=12
    
    return pages_dict
    
    

def get_related_products(product):
    company = product.company
    return Product.objects.filter(company=company)

        
def filter_cart(request):
    total_price = 0;
    items = 0;
    try:
        cart = request.session.get('cart')
        items = len(cart)
        for item in cart:
            product = Product.objects.get(slug=item['slug'])
            total_price += (product.price * item['quantity'])
    except:
        return None

    return {'total_price': total_price, 'no_of_items': items }


