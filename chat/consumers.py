import base64
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from users.models import User
from chat.models import Message

class ChatConsumer(WebsocketConsumer):
	def connect(self):
		user = self.scope['user']
		print(user, user.is_authenticated)

		if not user.is_authenticated:
			return

		self.username = user.username
		
		async_to_sync(self.channel_layer.group_add)(self.username, self.channel_name)
		
		self.accept()

	def disconnect(self, close_code):
		async_to_sync(self.channel_layer.group_discard)(self.username, self.channel_name)

	def receive(self, text_data):
		data = json.loads(text_data)
		message = data['message']
		async_to_sync(self.channel_layer.group_send)(
			self.username, {
				'type': 'chat.message', 
				'message': message,
			})

	def chat_message(self, event):
		message = event['message']
		self.send(text_data=json.dumps({
			'message': message
		}))

	def receive_message_send(self, data):
		user = self.scope['user']
		chatId = data.get('chatId')
		message_text = data.get('message')
		try:
			message = Message.objects.get(id=chatId)
		except Message.DoesNotExist:
			print('Error: couldnt find connection')
			return

		message = Message.objects.create(sender=user, receiver=message, message_text=message)
		# Get recipient friend
		recipient = message.sender
		if message.sender == user:
			recipient = message.receiver

		# Send new message back to sender
		serialized_message = MessageSerializer(
			message,
			context={
				'user': user
			}
		)
		serialized_friend = UserSerializer(recipient)
		data = {
			'message': serialized_message.data,
			'friend': serialized_friend.data
		}
		self.send_group(user.username, 'message.send', data)

		# Send new message to receiver
		serialized_message = MessageSerializer(
			message,
			context={
				'user': recipient
			}
		)
		serialized_friend = UserSerializer(user)
		data = {
			'message': serialized_message.data,
			'friend': serialized_friend.data
		}
		self.send_group(recipient.username, 'message.send', data)