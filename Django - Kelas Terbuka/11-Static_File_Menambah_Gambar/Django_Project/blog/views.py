from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': "Blog",
		'subtitle': "Halo selamat datang di Rasyidev's Blog!",
		'banner': "img/banner_blog.png"
	}
	return render(request, 'index.html', context)