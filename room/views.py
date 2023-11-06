from .models import Chat, Message
from constants import TOP_MESSAGES
from django.contrib.auth.models import User
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
    all_rooms = Chat.objects.all()
    return render(request, 'room/rooms.html', {'rooms': all_rooms})


@login_required
def get_users(request):
    all_users = User.objects.all()
    return render(request, 'room/inbox.html', {'users': all_users})


@login_required
def user(request, slug):
    current_user = User.objects.get(username=slug)
    return render(request, 'room/user.html', {'current_user': current_user, 'other_user': slug})


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
    room = Chat.objects.get(slug=slug)
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
    # import pdb
    # pdb.set_trace()
    if request.method == "GET":
        return render(request, 'room/room_form.html')
    if request.method == 'POST':
        name = request.POST['name']
        slug = request.POST['slug']
        room = Chat(name=name, slug=slug)
        room.save()
        return redirect('rooms')
