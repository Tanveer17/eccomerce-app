"""ecommerce_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from product import urls as product_urls
from cart import urls as cart_urls
from user import urls as user_urls
from product.views import home,shop,single_product
from cart.views import add_to_cart, show_cart, remove_item_from_cart,checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(product_urls)),
    path('cart/',include(cart_urls)),
    path('user/',include(user_urls))
  ]
