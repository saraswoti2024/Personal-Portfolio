from django.db import models

# Create your models here.

gender_field=(
    ('male',"male"), 
    ('female','female'),
    ("other",'other')
)
class Users(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    gender=models.CharField(null=True,max_length=200)
    message=models.TextField()