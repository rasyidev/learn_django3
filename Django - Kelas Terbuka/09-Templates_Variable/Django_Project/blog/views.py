from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': "Blog",
		'kontributor': "Rasyidev"
	}
	return render(request, 'blog/index.html', context)

def cerita(request):
	context = {
		'title': "Cerita",
		'kontributor': "Meowee"
	}
	return render(request, 'blog/index.html', context)