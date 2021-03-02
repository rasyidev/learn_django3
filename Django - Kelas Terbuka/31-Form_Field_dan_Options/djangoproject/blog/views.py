from django.shortcuts import render, redirect

from .forms import PostForm
from .models import PostModel

# Create your views here.

def index(request):
   posts = PostModel.objects.all()
   context = {
      'page_title': "Post List", 
      'posts' : posts
   }
   return render(request, 'blog/index.html', context)

def create(request):
   post_form = PostForm(request.POST or None)
   if request.method == 'POST':
      if post_form.is_valid():
         post_form.save()
         print(request.method, request.POST.get('title'), post_form.is_valid())
         return redirect('blog:index')

   context = {
      'page_title': "Create Post",
      'post_form': post_form
   }
   return render(request, 'blog/create.html', context)