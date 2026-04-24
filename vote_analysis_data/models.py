from django.db import models

class Analysis_vote(models.Model):
    player_name=models.CharField(max_length=255)
    team_name=models.CharField(max_length=255)
   
# Create your models here.
    class Meta:
     verbose_name ="Analysis_vote"
     verbose_name_plural ="Analysis_vote"
def __str__(self):
      return  self.name