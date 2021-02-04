from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return HttpResponse("Hello, Kamu lagi ada di aplikasi polls nih, view index")
