"""studentscorner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('preview.urls', namespace="preview")),
    url(r'^', include('catalog.urls', namespace="catalog")),
    url(r'^cart/', include('cart.urls',namespace="cart")),
    url(r'^checkout/', include('checkout.urls',namespace="checkout")),
    url(r'^accounts/', include('accounts.urls',namespace="accounts")),
    url(r'^accounts/', include('django.contrib.auth.urls',namespace="accounts")),
]

handler404 = 'catalog.views.file_not_found_404'