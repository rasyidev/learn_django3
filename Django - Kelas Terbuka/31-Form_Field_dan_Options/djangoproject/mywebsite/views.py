from django.shortcuts import render

def index(request):
   context = {
      'page_title': "Home page"
   }
   return render(request, 'index.html', context)