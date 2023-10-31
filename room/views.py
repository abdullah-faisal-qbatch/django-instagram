from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import generics
from django.http import HttpResponse
from .models import Room
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def rooms(request):
    all_rooms = Room.objects.all()
    print(all_rooms)
    return render(request, 'room/rooms.html', {'rooms': all_rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
def add_room(request):
    if request.method == "GET":
        print("GET METHOD")
        print("********************************")
        return render(request, 'room/room_form.html')
    if request.method == 'POST':
        print("POST METHOD")
        print("********************************")
        name = request.POST['name']
        slug = request.POST['slug']
        room = Room(name=name, slug=slug)
        room.save()
        return redirect('room/rooms')
    # Redirect to a room list page
    # return render(request, 'room/room_form.html')


# @login_required
# def room_list(request):
#     rooms = Room.objects.all()
#     return render(request, 'room_list.html', {'rooms': rooms})


@login_required
class AddRoomView(generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'room/room_form.html')

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        slug = request.POST['slug']
        room = Room(name=name, slug=slug)
        room.save()
        return redirect('')  # Redirect to a room list page
