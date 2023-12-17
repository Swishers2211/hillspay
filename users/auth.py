from django.contrib.auth.backends import BaseBackend
from users.models import User
from django.db.models import Q

class Email(BaseBackend):
	def get_user(self, user_id):
		try:
			return User.objects.get(id=user_id)
		except User.DoesNotExist:
			return None

	def authenticate(self, request, username=None, password=None):
		user = User
		try:
			user = User.objects.get(Q(email__exact=username))
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None