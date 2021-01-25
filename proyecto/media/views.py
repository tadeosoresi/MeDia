from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
''''def index(request):
    return render(request, 'index.html')'''

def contacto(request):
    if request.method == 'POST':

       name = request.POST['nombre']
       num = request.POST['telefono']
       message = request.POST['mensaje'] + ' ' + request.POST['email']
       email_from = settings.EMAIL_HOST_USER
       recipient_list = ['tadeosoresi23@outlook.com']

       send_mail(name, num, message, email_from, recipient_list)
       return(request, 'success.html')
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')