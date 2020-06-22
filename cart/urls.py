from django.urls import path

from .views import show_cart,add_to_cart, remove_item_from_cart, checkout


urlpatterns = [
         path('',show_cart,name='show_cart'),
         path('remove/<slug>/<int:quantity>',remove_item_from_cart,name='remove_item'),
         path('single/add_to_cart/',add_to_cart,name='add_to_cart'),
         path('checkout',checkout,name='checkout')
]
