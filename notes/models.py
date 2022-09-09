from django.db import models

class Notes(models.Model):    
    text = models.CharField(max_length=500)    
    date = models.DateTimeField(auto_now_add=True)