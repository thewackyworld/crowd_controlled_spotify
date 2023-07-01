from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import songitem

# Create your views here.

def listView(request):
    all_songs = songitem.objects.all()
    return render(request, 'musiclist.html',
                  {'songs': all_songs})

def addsong(request):
    #create a new song item
    newsong = songitem(songname = request.POST['songname'], artist= request.POST['artist'], votes = 1)
    #save new song
    newsong.save()
    #redirect back to /list/ 
    return HttpResponseRedirect('/list/')

def addvote(request, song_id):
    vote_to_add = songitem.objects.get(id = song_id)
    vote_to_add.votes = vote_to_add.votes + 1
    vote_to_add.save()
    return HttpResponseRedirect('/list/')
    