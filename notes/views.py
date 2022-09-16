from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NoteForm
from .models import Notes


def index(request):
    if request.method == 'POST': #method is post as we are inputting data
        form = NoteForm(request.POST) #creating an instance for this form
        newNote = form.save(commit=False) #creating the object but not committing yet - may not be needed
        #newNote.text = request.text, not too sure why this is not needed maybe cuz its a post request?
        newNote.save() #creating the note object
        notes = Notes.objects.all().order_by('-date')
        return render(request, "home.html", {'form':NoteForm, 'notes':notes})

    else:
        notes = Notes.objects.all().order_by('-date')
    return render(request, "home.html", {'form':NoteForm, 'notes':notes})

def delete(request, id):
     note = Notes.objects.get(id=id)
     note.delete()
     return HttpResponseRedirect(reverse('index'))






