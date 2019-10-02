from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
def register(request):
    global context
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect('')
    else:
                form = RegistrationForm()
                context = {'form':form}


    return render(request, 'users/register.html', context)

