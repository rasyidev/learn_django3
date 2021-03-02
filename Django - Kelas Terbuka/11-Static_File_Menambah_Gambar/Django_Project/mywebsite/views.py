from django.shortcuts import render

def index(request):
	context = {
		'title': "Home",
		'subtitle': "Halo selamat datang di Rasyidev's Home!",
		'banner': "img/banner_home.png"
	}

	return render(request, 'index.html', context)