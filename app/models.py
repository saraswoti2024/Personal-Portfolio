from django.db import models

# Create your models here.

gender_field=(
    ('male',"male"), 
    ('female','female'),
    ("other",'other')
)
class Users(models.Model):
    fullname=models.CharField(max_length=55)
    email=models.EmailField(unique=True)
    gender=models.CharField(choices=gender_field,null=True,max_length=200)
    message=models.TextField()