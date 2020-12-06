from django.db import models
from datetime import datetime

# Create your models here.
class Contactinfo(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length= 250)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__ (self):
        return self.name

class RegisterationForm(models.Model):
    username = models.CharField(max_length= 40)
    useremail = models.EmailField()
    phonenum = models.IntegerField()
    state = models.CharField(max_length= 200, blank=True)
    dob = models.DateTimeField(blank=True)
    password = models.CharField(max_length=1050)

    def __str__(self):
        return self.username