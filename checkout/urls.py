from studentscorner import settings
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.show_checkout, {'template_name':'checkout/checkout.html'}, name="checkout"),
	url(r'^receipt/$', views.receipt, {'template_name':'checkout/receipt.html'}, name="checkout_receipt"),
]
