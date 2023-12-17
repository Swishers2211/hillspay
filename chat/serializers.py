from rest_framework import serializers

from users.models import User
from chat.models import Connection, Message

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'name',
        ]

    def get_name(self, obj):
        fname = obj.username.capitalize()
        return fname

class SearchSerializer(UserSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'status'
        ]
    
    def get_status(self, obj):
        if obj.pending_them:
            return 'pending-them'
        elif obj.pending_me:
            return 'pending-me'
        elif obj.connected:
            return 'connected'
        return 'no-connection'

class RequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'message_time'
        ]


class FriendSerializer(serializers.ModelSerializer):
    friend = serializers.SerializerMethodField()
    preview = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        fields = [
            'id',
            'friend',
            'preview',
            'updated'
        ]

    def get_friend(self, obj):
        # If Im the sender
        if self.context['user'] == obj.sender:
            return UserSerializer(obj.receiver).data
        # If Im the receiver
        elif self.context['user'] == obj.receiver:
            return UserSerializer(obj.sender).data
        else:
            print('Error: No user found in friendserializer')

    def get_preview(self, obj):
        default = 'New connection'
        if not hasattr(obj, 'latest_text'):
            return default
        return obj.latest_text or default

    def get_updated(self, obj):
        if not hasattr(obj, 'latest_created'):
            date = obj.updated
        else:
            date = obj.latest_created or obj.updated
        return date.isoformat()

class MessageSerializer(serializers.ModelSerializer):
    is_me = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'id',
            'is_me',
            'message_text',
            'message_time'
        ]

    def get_is_me(self, obj):
        return self.context['user'] == obj.user
