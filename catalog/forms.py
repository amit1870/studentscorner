from django import forms
from .models import *

class ProductAdminForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude = ('created_at','updated_at',)

	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero.')
		return self.cleaned_data['price']
		

