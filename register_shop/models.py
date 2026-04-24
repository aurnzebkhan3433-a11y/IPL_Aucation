from django.db import models

class Register_shop(models.Model):
    names=models.CharField(max_length=255)
    numbers=models.IntegerField()
    emails=models.EmailField()
    passwords=models.CharField()
   
    class Meta:
     verbose_name ="Register_shop"
     verbose_name_plural ="Register_shop"

    def __str__(self):
      return  self.names


# Create your models here.
