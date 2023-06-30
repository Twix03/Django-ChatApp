from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def chatroom(request, name):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=name)
    return render(
        request,
        "room.html",
        {"room": name, "username": username, "room_details": room_details},
    )


def checkview(request):
    roomname = request.POST["room_name"]
    username = request.POST["username"]
    print(request.POST["username"])

    if Room.objects.filter(name=roomname).exists():
        return redirect("/" + roomname + "/?username=" + username)
    else:
        newRoom = Room.objects.create(name=roomname)
        newRoom.save()
        return redirect("/" + roomname + "/?username=" + username)


def send(request):
    content = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]

    newMessage = Message.objects.create(content=content, user=username, room=room_id)
    newMessage.save()
    return HttpResponse("OK")


def getmessages(request, name):
    currRoom = Room.objects.get(name=name)
    messages = Message.objects.filter(room=currRoom.id)
    return JsonResponse({"messages": list(messages.values())})
