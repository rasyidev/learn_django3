from django.shortcuts import render

def index(request):
	context = {
		'greetings': "Good Morning",
		'name': "Habib"
	}
	return render(request, 'index.html', context)