from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as dj_logout
from django.contrib.auth.decorators import login_required



def index(request):
   context = {
      'page_title': "Home Page"
   }
   return render(request, 'index.html', context)

def user_login(request):
   if(request.method == 'POST'):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)

      print(user)
      if user is not None:
         if(user.is_active):
            login(request, user)
            return redirect('user_area')
         else:
            return redirect('home')

   context ={
      'page_title': "Login Page"
   }

   if(request.method == 'GET'):
      if(request.user.is_authenticated):
         return redirect('user_area')
      else:
         return render(request, 'login.html', context)

@login_required
def logout(request):
   context = {
      'page_title': "Halaman Logout"
   }
   if request.method == 'POST':
      print(request.POST['logout'] == 'Submit')
      if request.POST['logout'] == 'Submit':
         dj_logout(request)
         return redirect('home')
   return render(request, 'logout.html', context)

@login_required
def user_area(request):
   context = {
      'page_title': "User Area"
   }
   return render(request, 'user_area.html', context)