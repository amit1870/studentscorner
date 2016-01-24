from django.shortcuts import render , get_object_or_404

def file_not_found_404(request):
	page_title = "Page Not Found"
	return render(request,"catalog/404.html",)