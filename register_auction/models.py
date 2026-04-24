from django.db import models

# Create your models here.
class Datasave(models.Model):
    name=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    email=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    class Meta:
        db_table = "Datasave"