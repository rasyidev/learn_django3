from django.shortcuts import render

def index(request):
	context = {
		'title': "Home",
		'subtitle': "Wellcome to Rasyidev Home",
		'nav': [
			['/', 'Home'],
			['blog/', 'Blog'],
			['contact/', 'Contact'],
			['about/', 'About']
		]
	}
	return render(request, 'index.html', context)

def blog(request):
	context = {
		'title': "Blog",
		'subtitle': "Wellcome to Rasyidev Blog",
		'nav': [
			['/', 'Home'],
			['/blog/', 'Blog'],
			['/contact/', 'Contact'],
			['/about/', 'About']
		]
	}
	return render(request, 'index.html', context)

def contact(request):
	context = {
		'title': "Contact",
		'subtitle': "Wellcome to Rasyidev Contact",
		'nav': [
			['/', 'Home'],
			['/blog/', 'Blog'],
			['/contact/', 'Contact'],
			['/about/', 'About']
		]
	}
	return render(request, 'index.html', context)

def about(request):
	context = {
		'title': "About",
		'subtitle': "Wellcome to Rasyidev About",
		'nav': [
			['', 'Home'],
			['/blog/', 'Blog'],
			['/contact/', 'Contact'],
			['/about/', 'About']
		]
	}
	return render(request, 'index.html', context)