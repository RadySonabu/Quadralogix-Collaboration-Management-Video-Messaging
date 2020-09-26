from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.conf import settings
from .models import Room

# Create your views here.

def IndexView(request, slug):
	room = Room.objects.last()
	return render(request,'common/index.html', {'apiKey':settings.TOK_KEY, 'session':room.session, 'token':room.token, 'slug': room.slug})
