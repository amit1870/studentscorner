from django import forms
from .models import Order
import datetime
import re

def cc_expire_years():
	current_year = datetime.datetime.now().year
	years = range(current_year, current_year+12)
	return [(str(x),str(x)) for x in years]

def cc_expire_months():
	months = []
	for month in range(1,13):
		if len(str(month)) == 1:
			numeric = '0' + str(month)
		else:
			numeric = str(month)

		months.append((numeric, datetime.date(2015, month, 1).strftime('%B')))
	return months

CARD_TYPES = (('Mastercard','Mastercard'),
				('VISA','VISA'),
				('AMEX','AMEX'),
				('Discover','Discover'),)

def strip_non_numbers(data):
	""" gets rid of all non-number characters """
	non_numbers = re.compile('\D')
	return non_numbers.sub('',data)

# Gateway test credit cards won't pass this validation
def cardLuhnChecksumIsValid(card_number):
	""" checks to make sure that the card passes a luhn mod-10 checksum """
	sum = 0
	num_digits = len(card_number)
	oddeven = num_digits & 1
	for count in range(0, num_digits):
		digit = int(card_number[count])
		if not (( count & 1 ) ^ oddeven ):
			digit = digit * 2
		if digit > 9:
			digit = digit - 9
		sum = sum + digit
		return ( (sum % 10) == 0 )

class CheckoutForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CheckoutForm, self).__init__(*args, **kwargs)
		# override default attributes
		for field in self.fields:
			self.fields[field].widget.attrs['size'] = '30'
			self.fields['shipping_state'].widget.attrs['size'] = '3'
			self.fields['shipping_zip'].widget.attrs['size'] = '6'
			self.fields['billing_state'].widget.attrs['size'] = '3'
			self.fields['billing_zip'].widget.attrs['size'] = '6'
			self.fields['credit_card_type'].widget.attrs['size'] = '1'
			self.fields['credit_card_expire_year'].widget.attrs['size'] = '1'
			self.fields['credit_card_expire_month'].widget.attrs['size'] = '1'
			self.fields['credit_card_cvv'].widget.attrs['size'] = '5'

	class Meta:
		model = Order 
		exclude = ('status','ip_address','user','transaction_id')

	credit_card_number = forms.CharField()
	credit_card_type = forms.CharField(widget=forms.Select(choices=CARD_TYPES))
	credit_card_expire_month = forms.CharField(widget=forms.Select(choices=cc_expire_months()))
	credit_card_expire_year = forms.CharField(widget=forms.Select(choices=cc_expire_years()))
	credit_card_cvv = forms.CharField()

	def clean_credit_card_number(self):
		cc_number = self.cleaned_data['credit_card_number']
		stripped_cc_number = strip_non_numbers(cc_number)
		if not cardLuhnChecksumIsValid(stripped_cc_number):
			raise forms.ValidationError('The credit card you entered is invalid.')

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		stripped_phone = strip_non_numbers(phone)
		if len(stripped_phone) < 10:
			raise forms.ValidationError('Enter a valid phone number with area code.(e.g.8377894662)')
		return self.cleaned_data['phone']

class CheckoutForm(forms.ModelForm):

	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email',
		'class':'form-control'}),error_messages={'invalid':'Please enter a valid email.'},)

	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mobile Number',
		'class':'form-control'}),error_messages={'invalid':'Please enter a Mobile Number.'},)

	shipping_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping Name',
		'class':'form-control','maxlength':30}),error_messages={'invalid':'Please enter a Shipping Name.'},)

	shipping_address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping Address1',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping Address1.'},)

	shipping_address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping Address2',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping Address2.'},)

	shipping_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping City',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping City'},)

	shipping_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping State',
		'class':'form-control','maxlength':3}),error_messages={'invalid':'Please enter a Shipping State'},)

	shipping_zip = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping Zip',
		'class':'form-control','maxlength':6}),error_messages={'invalid':'Please enter a Shipping Zip'},)

	shipping_country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shipping Country',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping Country'},)

	billing_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing Name',
		'class':'form-control','maxlength':30}),error_messages={'invalid':'Please enter a Shipping Name.'},)

	billing_address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing Address1',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping Address1.'},)

	billing_address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing Address2',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping Address2.'},)

	billing_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing City',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping City'},)

	billing_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing State',
		'class':'form-control','maxlength':3}),error_messages={'invalid':'Please enter a Shipping State'},)

	billing_zip = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing Zip',
		'class':'form-control','maxlength':6}),error_messages={'invalid':'Please enter a Shipping Zip'},)

	billing_country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Billing Country',
		'class':'form-control','maxlength':100}),error_messages={'invalid':'Please enter a Shipping Country'},)

	credit_card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Credit Card Number',
		'class':'form-control','maxlength':16}),error_messages={'invalid':'Please enter a valid Credit Card Number.'},)

	credit_card_expire_month = forms.CharField(widget=forms.Select(choices=CARD_TYPES,attrs={
		'class':'form-control'}),)

	credit_card_type = forms.CharField(widget=forms.Select(choices=cc_expire_months(),attrs={
		'class':'form-control'}),)

	credit_card_expire_year = forms.CharField(widget=forms.Select(choices=cc_expire_years(),attrs={
		'class':'form-control'}),)

	credit_card_cvv = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'CVC',
		'class':'form-control','maxlength':3}),error_messages={'invalid':'Please enter a valid Enter CVC.'},)

	def __init__(self, *args, **kwargs):
		super(CheckoutForm, self).__init__(*args, **kwargs)
		# override default attributes
		# for field in self.fields:
		# 	self.fields[field].widget.attrs['size'] = '30'
		# 	self.fields['shipping_state'].widget.attrs['size'] = '3'
		# 	self.fields['shipping_state'].widget.attrs['size'] = '3'
		# 	self.fields['shipping_zip'].widget.attrs['size'] = '6'
		# 	self.fields['billing_state'].widget.attrs['size'] = '3'
		# 	self.fields['billing_state'].widget.attrs['size'] = '3'
		# 	self.fields['billing_zip'].widget.attrs['size'] = '6'
		# 	self.fields['credit_card_type'].widget.attrs['size'] = '1'
		# 	self.fields['credit_card_expire_year'].widget.attrs['size'] = '1'
		# 	self.fields['credit_card_expire_month'].widget.attrs['size'] = '1'
		# 	self.fields['credit_card_cvv'].widget.attrs['size'] = '5'

	class Meta:
		model = Order 
		exclude = ('status','ip_address','user','transaction_id')



	

	def clean_credit_card_number(self):
		cc_number = self.cleaned_data['credit_card_number']
		stripped_cc_number = strip_non_numbers(cc_number)
		if not cardLuhnChecksumIsValid(stripped_cc_number):
			raise forms.ValidationError('The credit card you entered is invalid.')

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		stripped_phone = strip_non_numbers(phone)
		if len(stripped_phone) < 10:
			raise forms.ValidationError('Enter a valid phone number with area code.(e.g.8377894662)')
		return self.cleaned_data['phone']
