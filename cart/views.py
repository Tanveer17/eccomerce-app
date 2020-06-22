from django.shortcuts import render,redirect,reverse
from django.http.response import HttpResponse
from .forms import CartForm
from .classes import SessionCart

from product.models import Product
from product.views import filter_cart
# Create your views here.

def add_to_cart(request):
    if request.method == 'GET': 
        form = CartForm(request.GET)
        if form.is_valid():
            slug = form.cleaned_data['slug']
            quantity = form.cleaned_data['quantity']
            cart_item = SessionCart(slug,quantity).serialize()
            if request.session.get('cart').__contains__(cart_item):
                index = request.session.get('cart').index(cart_item) 
                request.session.get('cart')[index]['quantity'] += quantity
            else:
                request.session.get('cart').append(cart_item)

            request.session.modified=True
            print('cart: ',request.session.get('cart'))
            return redirect(reverse('single_product',
                kwargs={'slug':slug}))
        else:
            return redirect(reverse('single_product',kwargs=
                    {'form':form,'slug':form.cleaned_data['slug']}))


def show_cart(request):
    cart = filter_cart(request)
    if request.method == 'POST':
        if request.POST.get('proceed'):
            return render(request,'cart/checkout.html',
                    {'cart':cart})

   
    items_in_cart = get_items_in_cart(request)    
    return render(request,
            'cart/cart.html',
            {'items_in_cart':items_in_cart,
                'cart':cart})

def remove_item_from_cart(request,slug,quantity):
    
    item = SessionCart(slug,quantity)
    print('remove',item.serialize())
    print(request.session['cart'])
    request.session['cart'].remove(item.serialize())
    request.session.modified=True
    return redirect(reverse('show_cart'))
                


def get_items_in_cart(request):
    items_in_cart = []

    try:
       cart = request.session.get('cart')
       print(cart)

       for item in cart:
           cart_item = {}
           product = Product.objects.get(slug=item['slug'])
           print(product)
           name = product.name
           model = product.model
           pic = product.pic
           price = product.price
           print('before quantity')
           quantity = item['quantity']
           total_price = (quantity * price)
           
           cart_item['name'] = name
           cart_item['model'] = model
           cart_item['slug'] = item['slug']
           cart_item['pic'] = pic
           cart_item['price'] = price
           cart_item['quantity'] = quantity
           cart_item['total_price'] = total_price

           items_in_cart.append(cart_item)

    except:
        print('exception')
        return None

    return items_in_cart

def checkout(request):
    return render(request,
            'cart/checkout.html')
