from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': "About",
		'subtitle': "Halo selamat datang di Rasyidev's About!",
		'banner': "img/banner_about.png"
	}
	return render(request, 'index.html', context)