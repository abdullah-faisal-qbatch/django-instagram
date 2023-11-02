from .models import Room, Message
from constants import TOP_MESSAGES
from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def rooms(request):
    """
    Renders a list of all available rooms.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML page displaying a list of all available rooms.
    """
    all_rooms = Room.objects.all()
    print(all_rooms)
    return render(request, 'room/rooms.html', {'rooms': all_rooms})


@login_required
def room(request, slug):
    """
    Renders the room page with room details and messages.

    Args:
        request: The HTTP request object.
        slug (str): The unique slug of the room to display.

    Returns:
        A rendered HTML page showing room details and messages associated with the specified room.
    """
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:TOP_MESSAGES]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
def add_room(request):
    """
    Handles the addition of a room to the system.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, it renders the 'room_form.html' template.
        If the request method is POST, it processes the form data, creates a new room,
        and redirects to the 'room/rooms' page.

    """
    if request.method == "GET":
        return render(request, 'room/room_form.html')
    if request.method == 'POST':
        name = request.POST['name']
        slug = request.POST['slug']
        room = Room(name=name, slug=slug)
        room.save()
        return redirect('room/rooms')


@login_required
class AddRoomView(generics.CreateAPIView):
    """
    View for adding a new room.

    This view handles both GET and POST requests to display the room form and create a new room,
    respectively.

    Methods:
    - get: Renders the room creation form for GET requests.
    - post: Processes the submitted form data and creates a new room for POST requests.

    Args:
        request: The HTTP request object.

    Returns:
        - For GET requests, it renders the 'room_form.html' template.
        - For POST requests, it creates a new room based on the submitted data and redirects to a specified URL.
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'room/room_form.html')

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        slug = request.POST['slug']
        room = Room(name=name, slug=slug)
        room.save()
        return redirect('')
