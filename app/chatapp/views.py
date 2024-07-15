from django.shortcuts import render
from .models import ChatRoom
# Create your views here.


def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {"chatrooms": chatrooms})
