from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model): 
  title = models.CharField(max_length=250) 
<<<<<<< HEAD
  created_date =  models.DateTimeField(default=datetime.datetime.now)
  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
=======
  
>>>>>>> 0615f270a6687ed080a45a8b22ad2ba69faebe38
  completed = models.BooleanField(default=False) 
 
  def __str__(self): 
    return self.title 


