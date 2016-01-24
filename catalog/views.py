from django.shortcuts import render , get_object_or_404
from .models import *
from django.core import urlresolvers
from cart import cart
from django.http import HttpResponseRedirect
from cart.forms import ProductAddToCartForm

def index(request,template_name='catalog/index.html'):
	page_title = "Food products for people ad for"
	return render(request,template_name,{'page_title':page_title})

def show_category(request,category_slug, template_name='catalog/catalog.html'):
	c = get_object_or_404(Category,slug=category_slug)
	products = c.product_set.all()
	page_title  = c.name 
	meta_keywords = c.meta_keywords
	meta_description = c.meta_description
	return render(request, template_name,{'page_title':page_title,'products':products,'c':c})

def show_product(request, product_slug, template_name='catalog/product.html'):
	p = get_object_or_404(Product, slug=product_slug)
	categories = p.categories.filter(is_active=True)
	page_title = p.name
	meta_keywords = p.meta_keywords
	meta_description = p.meta_description

	# evaluate the HTTP method
	if request.method == 'POST':
		postdata = request.POST.copy()
		print postdata
		form = ProductAddToCartForm(request, postdata)
		print form
		# check if posted data is valid 
		if form.is_valid():
			# add to cart and redirect to cart page
			cart.add_to_cart(request)

			# if test cookie worked, get rid of it
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()

			url = urlresolvers.reverse('cart:show_cart')
			return HttpResponseRedirect(url)
		# return render(request,'catalog/forerror.html',{'form':form})
	else:
		form = ProductAddToCartForm(request=request,label_suffix=':')

	# assign the hidden input the product slug
	form.fields['product_slug'].widget.attrs['value'] = p.slug

	# set the test cookie on our first GET request
	request.session.set_test_cookie()
	return render(request, template_name,{'page_title':page_title,'categories':categories,'p':p,'form':form})