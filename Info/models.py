from django.db import models

# Create your models here.
class Lead(models.Model):
    """
    
    """
    ContactPersonName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=12)
    Address = models.CharField(max_length=400)
    Source = models.CharField(max_length=50)
    CurrentStage = models.CharField(max_length=50)

class Followup(models.Model):
    """
    docstring
    """
    Lead = models.ForeignKey("Lead",on_delete=models.CASCADE)
    DateOfFollowup = models.DateField(auto_now=False, auto_now_add=False)
    Response = models.CharField(max_length=100)
    
    



    

