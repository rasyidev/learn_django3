from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as dj_logout


def index(request):
   
   if(request.method == 'POST'):
      username = request.POST['username']
      password = request.POST['password']

      user = authenticate(request, username=username, password=password)
      print(user)
      if user is not None:
         login(request, user)
         print(user)

   context = {
      'page_title': "Login Page"
   }
   return render(request, 'index.html', context)

def logout(request):
   dj_logout(request)
   return redirect('index')
   # context = {
   #    'page_title': "Halaman Logout"
   # }
   # if request.method == 'POST':
      # print(request.POST['logout'] == 'Submit')
   #    if request.POST['logout'] == 'Submit':
   #       logout(request)
   #    # return redirect('login')
   # return render(request, 'logout.html', context)