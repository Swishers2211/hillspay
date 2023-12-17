from django.urls import path

from chat.views import chats, dialog

app_name = 'chat'

urlpatterns = [
	path('?dialog/<str:username>/', dialog, name='dialog'),
	path('', chats, name='chats'),
]
