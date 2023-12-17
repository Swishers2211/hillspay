from django.shortcuts import render, Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template.loader import render_to_string
import json
import datetime
from itertools import chain

from users.models import User
from chat.models import Message

@login_required(login_url='/')
def chats(request):
    messages = (Message.objects.filter(sender=request.user, sender_visibility=True) | Message.objects.filter(receiver=request.user, receiver_visibility=True)).order_by('-message_time')
    users = []
    last_messages = []
    for message in messages:
        if message.sender != request.user:
            if not message.sender in users:
                users.append(message.sender)
                last_message = (Message.objects.filter(sender=message.sender, receiver=request.user) | Message.objects.filter(receiver=message.sender, sender=request.user)).order_by('-message_time')[:1]
                last_messages.append(last_message)
        if message.receiver != request.user:
            if not message.receiver in users:
                users.append(message.receiver)
                last_message = (Message.objects.filter(sender=message.receiver, receiver=request.user) | Message.objects.filter(receiver=message.receiver, sender=request.user)).order_by('-message_time')[:1]
                last_messages.append(last_message)
    last_messages_list = []
    for message_query in last_messages:
        for message in message_query:
            if not message.is_readed and message.receiver == request.user:
                last_messages_list.insert(0, message)
            else:
                last_messages_list.append(message)

    context = {
    	'messages': last_messages_list,
    }
    return render(request, 'chat/chats.html', context)

@login_required(login_url='/')
def dialog(request, username):
    companion = User.objects.get(username=username)
    messages = (Message.objects.filter(sender=request.user, receiver=companion, sender_visibility=True) | Message.objects.filter(receiver=request.user, sender=companion, receiver_visibility=True)).order_by('message_time')[:20]
    not_readed_messages = Message.objects.filter(receiver=request.user, sender=companion, is_readed=False)
    for message in not_readed_messages:
        message.is_readed = True
        message.save()

    context = {
    	'sort_messages': messages[::-1],
    }
    return render(request, 'chat/messages.html', context)