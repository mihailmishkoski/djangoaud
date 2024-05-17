from djangoProject.models import Musician, Album
from django.shortcuts import render, redirect
from djangoProject.forms import CreateMusician, CreateAlbum


def musicians(request):
    musicians = Musician.objects.all()

    return render(request, "musicians.html", {"musicians": musicians, "new_var": 1})


def add_musician(request):
    if request.method == "POST":
        musician = CreateMusician(request.POST)
        if musician.is_valid():
            musician.save()
            return redirect('musicians')
    else:
        musician = CreateMusician()

    return render(request, "add_musician.html", {"form": musician})


def add_album(request):
    if request.method == "POST":
        album = CreateAlbum(request.POST)
        if album.is_valid():
            album.save()
            return redirect('albums')
    else:
        album = CreateAlbum()

    return render(request, "add_album.html", {"form": album})


def albums(request):
    albums = Album.objects.all()

    return render(request,"albums.html", {"albums": albums, "new_var": 1})

