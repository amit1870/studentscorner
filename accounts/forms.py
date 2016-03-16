from django import forms
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)

class MyAuthenticationForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username',
		'class':'form-control','maxlength':30}),error_messages={'invalid':'Please enter a valid username.'},)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password',
		'class':'form-control'}),error_messages={'invalid':'Please enter a valid password.'},)
	
	# override the default __init__ so we can set the request 
	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		super(MyAuthenticationForm,self).__init__(*args, **kwargs)

	# custom validation to check for cookies
	# def clean(self):
	# 	if self.request:
	# 		if not self.request.session.test_cookie_worked():
	# 			raise forms.ValidationError("Cookies must be enabled.")
	# 	return self.cleaned_data