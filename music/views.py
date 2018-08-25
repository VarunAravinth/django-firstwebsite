# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse('<h2> Album returned with id : '+album_id+' </h2>')

