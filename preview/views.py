from django.shortcuts import render

def home(request):
	return render(request,"preview/index.html")