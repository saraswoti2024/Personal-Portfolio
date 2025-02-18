from django.shortcuts import render,redirect
from .models import Users
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=='POST':
        datas = request.POST
        fullname1 = datas['namekovalue'] #new_VarName= datas['name_Attributevalue']
        email1 = datas['email']
        message1 = datas['message']
        gender1 = datas['gender']
        
        user = Users(fullname=fullname1,email=email1,message=message1,gender=gender1) ##database_ma_Vako_name = mathi_vako_name
        user.save() #value save database ma
        return HttpResponse("Submit Successful")
    return render(request,'home.html')