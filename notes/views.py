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
        newNote.user = request.user #the user that created the note
        newNote.save() #creating the note object
        notes = Notes.objects.filter(user=request.user).order_by('-date')
        return render(request, "home.html", {'form':NoteForm, 'notes':notes})

    else:
        notes = Notes.objects.filter(user=request.user).order_by('-date')
    return render(request, "home.html", {'form':NoteForm, 'notes':notes})

def delete(request, id):
     note = Notes.objects.get(id=id)
     note.delete()
     return HttpResponseRedirect(reverse('index')) #redirect to the index function which is defined above

def edit(request, id):
     chosen_note = Notes.objects.get(id=id)
     if request.method == 'GET':
        form = NoteForm(instance=chosen_note)
        return render(request, 'editnote.html', 
                      {'review': chosen_note,'form':form})
     else:
        form = NoteForm(request.POST, instance=chosen_note)
        form.save()
        return HttpResponseRedirect(reverse('index'))





