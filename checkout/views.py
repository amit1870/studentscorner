from django.shortcuts import render
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from .forms import CheckoutForm
from .models import Order, OrderItem
from . import checkout
from cart import cart
from accounts import profile

def show_checkout(request, template_name='checkout/checkout.html'):
	page_title = 'Checkout'
	
	if cart.is_empty(request):
		cart_url = urlresolvers.reverse('cart:show_cart')
		return HttpResponseRedirect(cart_url)

	if request.method == 'POST':
		postdata = request.POST.copy()
		form = CheckoutForm(postdata)
		print "comm"
		if form.is_valid():
			print "formvalid"
			response = checkout.process(request)
			order_number = response.get('order_number',0)
			error_message = response.get('message','')

			if order_number :
				request.session['order_number'] = order_number
				receipt_url = urlresolvers.reverse('checkout:receipt')
				return HttpResponseRedirect(receipt_url)
	else:
		if request.user.is_authenticated():
			user_profile = profile.retrieve(request)
			form = CheckoutForm(instance=user_profile)
		else:
			form = CheckoutForm()
	
	context = {'page_title':page_title, 'form':form}
	return render(request,template_name, context)

def receipt(request, template_name='checkout/receipt.html'):
	order_number = request.session.get('order_number','')
	if order_number :
		order = Order.objects.filter(id=order_number)[0]
		order_items = OrderItem.objects.filter(order=order)
		del request.session['order_number']
	else:
		cart_url = urlresolvers.reverse('cart:show_cart')
		return HttpResponseRedirect(cart_url)

	return render(request, template_name, {'order_number':order_number})





