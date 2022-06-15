from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
import random

def about(request):
    #return HttpResponse("<h1>Home World!</h1>")
    #rendering with context
    #context = { 'name' : "jitendra", 'sirname':'sharma' }
    return render(request, 'api/about.html')

def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    
    #rendering 
    return render(request, 'api/index.html')

def home(request):
    #return HttpResponse("<h1>Home World!</h1>")
    #rendering with context
    context = { 'name' : "jitendra", 'sirname':'sharma' }
    return render(request, 'api/home.html', context=context)


def form(request):
    #return HttpResponse("<h1>Home World!</h1>")
    #rendering with context
    #context = { 'name' : "jitendra", 'sirname':'sharma' }
    return render(request, 'api/form.html')

def password(request):
    
    
    length = int(request.GET.get('length')  )
      
    thepassword = ''
    ucflag = request.GET.get('uppercase')
    scflag = request.GET.get('special')
    nflag = request.GET.get('numbers')
    
    characters = list ('abcdefghijklmnopqrstuvwxyz')
    uchars=[]
    for x in range(26):
        uchars.append(random.choice(characters).upper())
    spclchars = list ('!@#$%^&*()')
    numbers = list('1234567890')    

    
    for x in range(length):
        thepassword+=random.choice(characters)
        if ucflag:
            thepassword+=random.choice(uchars)
        if scflag:
            thepassword+=random.choice(spclchars)
        if nflag:
            thepassword+=random.choice(numbers)        
        
    #return HttpResponse("<h1>Home World!</h1>")
    #rendering with context
    #context = { 'name' : "jitendra", 'sirname':'sharma' }
    return render(request, 'api/password.html', {'password':thepassword})
