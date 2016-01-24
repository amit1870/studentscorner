from django.shortcuts import render , get_object_or_404
from .models import *
from . import cart

def show_cart(request, template_name="cart/cart.html"):
	if request.method == "POST":
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			cart.remove_from_cart(request)
		if postdata['submit'] == 'Update':
			cart.update_cart(request)

	cart_items = cart.get_cart_items(request)
	cart_item_count = cart_items
	page_title = 'Shopping Cart'
	return render(request, template_name, {'page_title':page_title,'cart_items':cart_items,'cart_item_count':cart_item_count})



