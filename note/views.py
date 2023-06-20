from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'note/home.html' )

# post = form.save(commit = false)
# post.user = request.user
# 

# login required 

@login_required(login_url='login')
def create_note(request):
    note_form = NoteForm()
    notes = Note.objects.filter(note_owner = request.user )
    note_owner =  request.user
    if request.method == "POST":
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            formuser = note_form.save(commit=False)
            formuser.note_owner = request.user
            if formuser.note_title or formuser.note_content != "":
                formuser.save()
            context = {
                'notes': notes
            }
            return redirect('journal')
        # else:
        #     return render(request, 'note/home.html')
        
    context = {
        'note_form': note_form, 
        'notes'   : notes,
        'note_owner': note_owner,
    }
        
    return render(request, 'note/note.html', context)
        

@login_required(login_url='login')
def edit_note(request, pk):
    note = Note.objects.get(id = pk)

    noteform =NoteForm(instance=note)
    if request.method == 'POST':
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            confirm = note_form.save(commit=False)
            if confirm != "":
                confirm.save()
                
            return redirect('journal')
        
    context = {
        'noteform': noteform,
        'note' : note
    }
    return render(request, 'note/update.html', context)


@login_required(login_url="login")
def delete_note(request, pk):
    note  = Note.objects.get(id = pk)
    if request.method == "POST":
        note.delete()
        return redirect('journal')
    
    context = {
        'note' : note
    }
    return render(request, 'note/delete.html', context)


@login_required(login_url="login")
def read_note(request, pk):
    note = Note.objects.get(id = pk)
    context = {
        'note': note
    }
    return render(request, 'note/read.html', context)