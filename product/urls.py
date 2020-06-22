from django.urls import path
from .views import home, shop, single_product

urlpatterns = [
         path('',home,name='home'),
         path('shop/<int:page_number>',shop,name='shop_items_page'),
         path('shop/single/<slug>',single_product,name='single_product')
]
        
