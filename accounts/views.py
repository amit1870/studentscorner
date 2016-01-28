from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderItem
from .forms import UserProfileForm
from . import profile

def register(request, template_name="account/registration/register.html"):
	if request.method == "POST":
		postdata = request.POST.copy()
		form = UserCreationForm(postdata)
		if form.is_valid():
			form.save()
			un = postdata.get('username','')
			pw = postdata.get('password1','')
			from django.contrib.auth import login, authenticate
			new_user = authenticate(username=un, password=pw)
			if new_user and new_user.is_active:
				login(request,new_user)
				url = urlresolvers.reverse('account:my_account')
				return HttpResponseRedirect(url)

	else:
		form = UserCreationForm()

	page_title = 'User Registration'
	context = {'page_title':page_title,'form':form}
	return render(request, template_name, context)

@login_required
def my_account(request, template_name="account/registration/my_account.html"):
	page_title = "My Account"
	orders = Order.objects.filter(user=request.user)
	name = request.user.username
	context = {'page_title':page_title,'orders':orders,'name':name}
	return render(request, template_name, context)

@login_required
def order_details(request, order_id, template_name="account/registration/order_details.html"):
	order = get_object_or_404(Order, id=order_id, user=request.user)
	page_title = "Order Details for Order #" + order_id
	order_items = OrderItem.objects.filter(order=order)
	context = {'page_title':page_title,'order_items':order_items}
	return render(request, template_name, context)

@login_required
def order_info(request, template_name="account/registration/order_info.html"):
	if request.method == "POST":
		postdata = request.POST.copy()
		form = UserProfileForm(postdata)
		if form.is_valid():
			profile.set()
			url = urlresolvers.reverse('accounts:my_account')
			return HttpResponseRedirect(url)
	else:
		user_profile = profile.retrive(request)
		form = UserProfileForm(instance=user_profile)

	page_title = "Edit Order Information"
	context = {'page_title':page_title,'form':form}
	return render(request, template_name, context)
