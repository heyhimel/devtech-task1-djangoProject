from django.shortcuts import render, HttpResponse, redirect
from models import loginModel

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        psw = request.POST.get('pswl')
        obj = loginModel(user = name, pasw = psw)
        obj.save()
    return render(request, 'login.html')

def login(request):
    for i in range(15):
        name = request.POST.get('uname')
        psw = request.POST.get('pswl')
        obj2=loginModel.objects.get(id=i+1)
        if(obj2.user==name and obj2.pasw==psw):
            return redirect('http://127.0.0.1:8000/dashboard')
    #return render(request, 'login.html')
