from django.conf.urls import url
from . import views
from studentscorner import settings
from django.contrib.auth.views import login, password_change, password_change_done
from forms import MyAuthenticationForm


urlpatterns = [
	
	url(r'^register/$', views.register,{ 'template_name':'registration/register.html'},name="register"),
	url(r'^my_account/$', views.my_account,{ 'template_name':'registration/my_account.html'},name="my_account"),
	url(r'^order_details/(?P<order_id>[-\w]+)/$', views.order_details,{ 'template_name':'registration/order_details.html'},name="order_details"),
	url(r'^order_info/$', views.order_info,{ 'template_name':'registration/order_info.html'},name="order_info"),

]

urlpatterns += [
	url(r'^login/$',login,{'template_name': 'registration/login.html','authentication_form':MyAuthenticationForm},name="login"),
	url(r'^password_change/$',password_change,{'template_name': 'registration/password_change_form.html'},name="password_change"),
	url(r'^password_change/done/$',password_change_done,{'template_name': 'registration/password_change_done.html'},name="password_change_done"),
]