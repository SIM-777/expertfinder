from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expert (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="experts")
    expert_name=models.CharField(max_length=120)
    expert_id=models.CharField(max_length=120)
    expert_affiliation=models.CharField(max_length=200)
    expert_interests=models.JSONField(max_length=500,null=True)
    expert_thumbnail=models.CharField(max_length=1000,null=True)
    expert_citations=models.IntegerField(null=True)
    id=models.AutoField(primary_key=True)
    class Meta:
      unique_together=(('user','expert_id'))
    def __str__(self):
        return self.expert_name  
class expert_report(models.Model):
    id=models.AutoField(primary_key=True)
    expert=models.ForeignKey(expert,on_delete=models.CASCADE,null=True)
    interests=models.CharField(max_length=1000)
    links=models.CharField(max_length=1000)
    
    def __str__(self):
        return f'Expert Report {self.id}'
    
