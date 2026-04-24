from django.db import models

# Create your models here.
class Login(models.Model):
    phone_number=models.IntegerField()
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.phone_number
    class Meta:
        db_table="Login"