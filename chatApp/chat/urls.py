from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkview", views.checkview, name="checkview"),
    path("<str:name>/", views.chatroom, name="room"),
    path('send', views.send, name="send"),
    path('getMessages/<str:name>/', views.getmessages, name="getmessages"),
]
