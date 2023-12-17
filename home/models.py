from django.db import models
from django.conf import settings

from users.models import User

class Role(models.Model):
	sub_role = models.CharField(max_length=160, verbose_name='Подзаголовок')
	violation = models.TextField(verbose_name='Нарушение')
	punishment = models.TextField(verbose_name='Наказание')

	class Meta:
		verbose_name = 'Правило'
		verbose_name_plural = 'Правила'

class Category_Game(models.Model):
	name = models.CharField(max_length=64, verbose_name='Категория игр')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def __str__(self):
		return f'Категория: {self.name}'

	class Meta:
		verbose_name = 'Категория игры'
		verbose_name_plural = 'Категория игр'

class Game(models.Model):
	name = models.CharField(max_length=64, verbose_name='Название игры')
	description = models.TextField(verbose_name='Описание игры', null=True, blank=True)
	image = models.ImageField(upload_to='product_image', verbose_name='Фото игры', null=True, blank=True)
	category_game = models.ForeignKey(Category_Game, on_delete=models.CASCADE, verbose_name='Категория игры', null=True, blank=True)
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'Игра: {self.name}'

	class Meta:
		verbose_name = 'Игра'
		verbose_name_plural = 'Игры'

class Category(models.Model):
	name = models.CharField(max_length=64, verbose_name='Название категории')
	description = models.TextField(verbose_name='Описание категории', null=True, blank=True)
	game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'{self.game.name} - {self.name}'

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
	
class PlatForm(models.Model):
	name = models.CharField(max_length=64)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'{self.name} -- {self.category.name}'

	class Meta:
		verbose_name = 'Платформа'
		verbose_name_plural = 'Платформы'

class SubCategory(models.Model):
	name = models.CharField(max_length=64, verbose_name='Название подкатегории')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'{self.name} -- {self.category.name} '

	class Meta:
		verbose_name = 'Подкатегория'
		verbose_name_plural = 'Подкатегории'

class Product(models.Model):
	short_description = models.CharField(verbose_name='Краткое описание', max_length=60)
	description = models.TextField(verbose_name='Подробное описание')
	price_for_1_piece = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена за 1 шт')
	availability = models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
	game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
	platform = models.ForeignKey(PlatForm, on_delete=models.CASCADE, verbose_name='Платформа')
	image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото товара')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'Товар: {self.short_description} -- Автор {self.user.username}'

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		if not self.price_for_1_piece:
			price_for_1_piece = self.price_for_1_piece()
			self.price_for_1_piece = price_for_1_piece['id']
		super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

class Category_Сurrency(models.Model):
	name = models.CharField(max_length=64, verbose_name='Название категории')
	description = models.TextField(verbose_name='Описание категории', null=True, blank=True)
	diversity = models.CharField(max_length=15, verbose_name='Единицы валют')
	game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'{self.game.name} - {self.name}'

	class Meta:
		verbose_name = 'Внутриигровая валюта'
		verbose_name_plural = 'Внутриигровые валюты'

class PlatForm_Currency(models.Model):
	name = models.CharField(max_length=64)
	currency = models.ForeignKey(Category_Сurrency, on_delete=models.CASCADE, verbose_name='Категория валюты')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'{self.name} -- {self.currency.name} -- {self.currency.game.name}'

	class Meta:
		verbose_name = 'Платформа валюты'
		verbose_name_plural = 'Платформы валют'

class Product_Сurrency(models.Model):
	price_for_1_piece = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена за 1 шт')
	availability = models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')
	currency = models.ForeignKey(Category_Сurrency, on_delete=models.CASCADE, verbose_name='Категория валюты')
	game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
	platform_currency = models.ForeignKey(PlatForm_Currency, on_delete=models.CASCADE, verbose_name='Платформа валюты')
	image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото товара')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

	def __str__(self):
		return f'Валюта - {self.currency.name} -- игра {self.game.name}: {self.platform_currency.name} -- продавец {self.user.username} -- наличие {self.availability} -- цена {self.price_for_1_piece}'

	class Meta:
		verbose_name = 'Товар - валюта'
		verbose_name_plural = 'Товары - валюты'

class Basket(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	availability = models.PositiveSmallIntegerField(default=0)
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Карзина'
		verbose_name_plural = 'Карзины'

	def __str__(self):
		return f'Отложенное для {self.user.username} | товар: {self.product.name}'

	@classmethod
	def create_or_update(cls, product_id, user):
		products = Basket.objects.filter(user=user, product_id=product_id)

		if not products.exists():
			obj = Basket.objects.create(user=user, product_id=product_id)
			is_created = True
			return obj, is_created
		else:
			product = products.first()
			product.save()
			is_crated = False
			return product, is_crated

class DealManager(models.QuerySet):
	def total_sum(self):
		return sum(deal.sum() for deal in self)

	def total_availability(self):
		return sum(deal.availability for deal in self)

class Deal(models.Model):
	SALE = 0
	SUPPORT = 1
	REFOUND = 2
	STATUSES = (
		(SALE, 'Продан'),
		(SUPPORT, 'Поддержка'),
		(REFOUND, 'Возврат'),
	)
	short_description = models.CharField(verbose_name='Краткое описание', max_length=60)
	price_for_1_piece = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена за 1 шт')
	user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, verbose_name='Покупатель')
	saleman = models.ForeignKey(User, related_name='saleman', on_delete=models.CASCADE, verbose_name='Продавец')
	status = models.SmallIntegerField(default=SALE, choices=STATUSES, verbose_name='Статус')
	published = models.DateTimeField(auto_now_add=True)
	availability = models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')

	objects = DealManager.as_manager()

	class Meta:
		verbose_name = 'Сделка'
		verbose_name_plural = 'Сделки'

	def __str__(self):
		return f'Покутель - {self.user.username} | заказ - #{self.id} | продавец - {self.saleman.username}'

	def sum(self):
		return self.price_for_1_piece * self.availability


class Deal_CurrencyManager(models.QuerySet):
	def total_sum(self):
		return sum(deal_currency.sum() for deal_currency in self)

	def total_availability(self):
		return sum(deal_currency.availability for deal_currency in self)

class Deal_Currency(models.Model):
	SALE = 0
	SUPPORT = 1
	REFOUND = 2
	STATUSES = (
		(SALE, 'Продан'),
		(SUPPORT, 'Поддержка'),
		(REFOUND, 'Возврат'),
	)

	price_for_1_piece = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена за 1 шт')
	currency = models.ForeignKey(Category_Сurrency, on_delete=models.CASCADE, verbose_name='Категория валюты')
	quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')
	user = models.ForeignKey(User, related_name='user_currency', on_delete=models.CASCADE, verbose_name='Пользователь')
	saleman = models.ForeignKey(User, related_name='saleman_currency', on_delete=models.CASCADE, verbose_name='Продавец')
	status = models.SmallIntegerField(default=SALE, choices=STATUSES, verbose_name='Статус')
	published = models.DateTimeField(auto_now_add=True)
	availability = models.PositiveSmallIntegerField(default=1)

	objects = Deal_CurrencyManager.as_manager()

	class Meta:
		verbose_name = 'Сделка валюты'
		verbose_name_plural = 'Сделки валют'

	def __str__(self):
		return f'Покутель - {self.user.username} | заказ - #{self.id}  | продавец - {self.saleman.username}'

	def sum(self):
		return self.price_for_1_piece * self.availability

class Review(models.Model):
	SALE = 0
	SUPPORT = 1
	REFOUND = 2
	STATUSES = (
		(SALE, 'Продан'),
		(SUPPORT, 'Поддержка'),
		(REFOUND, 'Возврат'),
	)
	
	comment = models.TextField('Отзыв')
	user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE, verbose_name='Комментатор')
	price_for_1_piece = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена за 1 шт')
	game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
	saleman_comment = models.TextField('Ответ продавца')
	saleman = models.ForeignKey(User, related_name='saleman_comment', on_delete=models.CASCADE, verbose_name='Ответ продавца')
	status = models.SmallIntegerField(default=SALE, choices=STATUSES, verbose_name='Статус')
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'

	def __str__(self):
		return f'{self.published}, {self.user.username}, {self.game.name}, {self.price_for_1_piece}'
