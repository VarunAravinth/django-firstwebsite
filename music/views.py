# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>THIS IS A STATIC11 PAGE</h1>')

