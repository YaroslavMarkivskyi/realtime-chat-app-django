from django.shortcuts import render
from .models import ChatRoom, ChatMessage
# Create your views here.


def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {"chatrooms": chatrooms})


def chatroom(request, slug):
    chartoom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chartoom)[0:30]
    return render(request, 'chatapp/room.html', {'chartoom': chartoom, 'messages': messages})
