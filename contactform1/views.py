from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        sname=request.POST.get('sname')
        email = request.POST.get('email')
        organization = request.POST.get('organization')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = {

            'fname': fname,
            'sname': sname,
            'email': email,
            'organization': organization,
            'message': message,
            'phone': phone,
        }
        message = '''
          
          First Name:{}
          
          Last Name:{}
          
          Phone No:{}
          
          Organization: {}
          
          New Message:{}
          
          From : {}
          
          
        '''.format(data['fname'],data['sname'],data['phone'],data['organization'] ,data['message'], data['email'])
        send_mail(data['email'], message, '', ['tetra@gmail.com'])
    return render(request, 'index.html', {})
