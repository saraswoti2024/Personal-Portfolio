from django.shortcuts import render,redirect
from .models import Users
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
# Create your views here.

def home(request):
    if request.method=='POST':
        datas = request.POST
        fullname1 = datas['namekovalue'] #new_VarName= datas['name_Attributevalue']
        email1 = datas['email']
        message1 = datas['message']
        if 'gender' in request.POST:
            gender1 = datas['gender']
        try:
            user = Users(fullname=fullname1,email=email1,message=message1,gender=gender1) ##database_ma_Vako_name = mathi_vako_name
            user.full_clean()
            user.save() #value save database ma
            subject = "Thank you for getting in Touch!"
            message = render_to_string('gmail.html',{'name':fullname1,'date':datetime.now()})
            from_email = 'saraswotikhadka2k2@gmail.com'
            recipient_list = [email1] ##current database store submit
            emailmsg = EmailMessage(subject,message,from_email,recipient_list)
            emailmsg.send(fail_silently=True)
            messages.success(request,f'{fullname1} form submitted successfully!')
            return redirect('home')
        except Exception as e:
           messages.error(request,f'{str(e)}.TRY AGAIN')
           return redirect('home')
    return render(request,'home.html')
