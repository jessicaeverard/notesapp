from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NoteForm
from .models import Notes


def index(request):
    notes = Notes.objects.all()

    return render(request, "home.html", {'form':NoteForm, 'notes':notes})


def createnote(request):
    form = NoteForm(request.POST)
    newNote = form.save(commit=False)
    newNote.text = request.text
    newNote.save()
    return redirect('home.html', newNote)
