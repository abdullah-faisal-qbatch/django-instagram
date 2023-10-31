from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def rooms(request):
    all_rooms = Room.objects.all()
    print('Priting data:', all_rooms, 'Ending data')
    return render(request, 'room/rooms.html', {'rooms': all_rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
