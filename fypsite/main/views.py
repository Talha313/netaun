from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
 #from main.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def index(request):
    #return HttpResponse ("index.html")
    return render(request, 'main/index.html',{})

def login(request):
    return render(request, 'main/login.html')

def sign(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
           # return redirect('')
            return HttpResponseRedirect(reverse('main:index'))
            #return redirect('/index')
    else:
        form = UserCreationForm()
        arg={'form':form}
        return render(request, 'main/sign.html' ,arg)



# def login(request):
#     return render(request, 'main/login.html', {})
