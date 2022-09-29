from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):    
    text = models.CharField(max_length=500)    
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text