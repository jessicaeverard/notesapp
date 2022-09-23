from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def createaccount(request):
     return render(request, 'createaccount.html', {'form':UserCreationForm})
