from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

