from django.db import models

from django.contrib.auth.models import AbstractUser

class Country(models.Model):
	country = models.CharField(max_length=120, verbose_name='Страна')

	def __str__(self):
		return f'{self.country}'

	class Meta:
		verbose_name = 'Страна'
		verbose_name_plural = 'Страны'

class Gender(models.Model):
	gender = models.CharField(max_length=60, verbose_name='Страна')

	def __str__(self):
		return f'{self.gender}'

	class Meta:
		verbose_name = 'Пол'
		verbose_name_plural = 'Полы'

class User(AbstractUser):
	username = models.CharField(max_length=128, unique=True, verbose_name='Имя пользоателя')
	gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to='user_images', null=True, blank=True, verbose_name='Фото профиля')
	email = models.EmailField(unique=True, verbose_name='Электронная почта')
	country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна', null=True, blank=True)
	balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Баланс', null=True, blank=True)
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return f'{self.username}'

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

class BlackList(models.Model):
	user = models.ForeignKey(User, related_name='ban_user', on_delete=models.CASCADE, verbose_name='Кто банит?')
	banned_user = models.ForeignKey(User, related_name='banned_user', on_delete=models.CASCADE, verbose_name='Кого забанить?')
	cause = models.TextField(verbose_name='Причина')
	term = models.DateTimeField(verbose_name='Срок')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата занесения в черный список')

	def __str__(self):
		return f'{self.banned_user.username} находится в черном списке'

	class Meta:
		verbose_name = 'Черный список'
		verbose_name_plural = 'Черные списки'
