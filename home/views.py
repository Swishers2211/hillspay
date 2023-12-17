from django.shortcuts import render, Http404, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from home.models import Role, Review, Deal_Currency, Deal, Category, Game, SubCategory, Product, Category_Game, PlatForm, Basket, Category_Сurrency, PlatForm_Currency, Product_Сurrency
from users.models import User

from home.forms import ProductForm, Product_СurrencyForm

def home(request):
	context = {
		'games_count': Game.objects.all(),
		'games': Game.objects.all().order_by('-published')[:12],
		'categories': Category.objects.all(),
	}
	return render(request, 'home/index.html', context)

def role(request):
	return render(request, 'home/role.html', {'roles': Role.objects.all()})

def search_by_games(request):
	context = {
		'games': Game.objects.all().order_by('name'),
		'category_games': Category_Game.objects.all(),
	}
	return render(request, 'home/list_games.html', context)

def search_game(request):
	results = []
	if request.method == 'GET':
		query = request.GET.get('search')
		if query == '':
			queryset = None

	results = Game.objects.filter(Q(name__iregex=query)).order_by('name')
	context = {
		'game': Game.objects.all(),
		'category_games': Category_Game.objects.all(),
		'results': results,
		'query': query,
	}
	return render(request, 'home/search_game.html', context)

def detail_game(request, game_id):
	try:
		game = Game.objects.get(id=game_id)
	except:
		raise Http404('Игра не найдена!')
		
	context = {
		'game': game,
		'currencies': Category_Сurrency.objects.filter(game=game_id).order_by('name'),
		'categories': Category.objects.filter(game=game_id).order_by('name'),
		'products': Product.objects.filter(game=game_id).order_by('-published'),
		'products_currencies': Product_Сurrency.objects.filter(game=game_id).order_by('-published'),
	}
	return render(request, 'home/detail_game.html', context)

def search_product_game(request, game_id):
	try:
		game = Game.objects.get(id=game_id)
	except:
		raise Http404('Игра не найдена!')

	results = []
	if request.method == 'GET':
		query = request.GET.get('search')
		if query == '':
			queryset = None

	results = Product.objects.filter(Q(short_description__iregex=query), game=game_id).order_by('-published')
	context = {
		'game': game,
		'results': results,
		'query': query,
		'categories': Category.objects.filter(game=game_id).order_by('name'),
	}
	return render(request, 'home/search_products.html', context)

def detail_category(request, category_id):
	try:
		category = Category.objects.get(id=category_id)
	except:
		raise Http404('Категория не найдена!')

	context = {
		'category': category,
		'currencies': Category_Сurrency.objects.filter(game=category.game.id).order_by('name'),
		'categories': Category.objects.filter(game=category.game.id).order_by('name'),
		'subcategories': SubCategory.objects.filter(category=category).order_by('-published'),
		'products': Product.objects.filter(category_id=category).order_by('-published'),
		'platforms': PlatForm.objects.filter(category=category).order_by('name'),
	}
	return render(request, 'home/detail_category_products.html', context)

def search_product_category(request, category_id):
	try:
		category = Category.objects.get(id=category_id)
	except:
		raise Http404('Категория не найдена!')

	results = []
	if request.method == 'GET':
		query = request.GET.get('search')
		if query == '':
			queryset = None

	results = Product.objects.filter(Q(short_description__iregex=query), category=category_id).order_by('-published')
	context = {
		'category': category,
		'results': results,
		'query': query,
	}
	return render(request, 'home/search_products.html', context)

def detail_category_currency(request, currency_id):
	try:
		currency = Category.objects.get(id=currency_id)
	except:
		raise Http404('Категория не найдена!')

	context = {
		'currency': currency,
		'categories': Category.objects.filter(game=category.game.id).order_by('name'),
		'subcategories': SubCategory.objects.filter(category=category).order_by('-published'),
		'products': Product.objects.filter(category_id=category).order_by('-published'),
		'platforms': PlatForm.objects.filter(subcategory=category).order_by('name'),
	}
	return render(request, 'home/detail_category_products.html', context)

def detail_platform(request, platform_id):
	try:
		platform = PlatForm.objects.get(id=platform_id)
	except:
		raise Http404('Платформа не найдена!')

	subcategory = SubCategory.objects.get(id=platform.category.id)
	if subcategory:
		products = Product.objects.filter(platform=platform.id).order_by('-published')
	else:
		products = Product.objects.filter(subcategory=platform.id).order_by('-published')
	context = {
		'platform': platform,
		'subcategory': subcategory,
		'platforms': PlatForm.objects.filter(category=platform.category.id),
		'categoriess': Category.objects.filter(game=platform.category.id).order_by('name'),
		'subcategories': SubCategory.objects.filter(category=platform.category.id).order_by('-published'),
		'products': products,
	}
	return render(request, 'home/detail_platform.html', context)

def search_product_platform(request, platform_id):
	try:
		platform = PlatForm.objects.get(id=platform_id)
	except:
		raise Http404('Платформа не найдена!')

	results = []
	if request.method == 'GET':
		query = request.GET.get('search')
		if query == '':
			queryset = None

	results = Product.objects.filter(Q(short_description__iregex=query), platform=platform_id).order_by('-published')
	context = {
		'platform': platform,
		'results': results,
		'query': query,
	}
	return render(request, 'home/search_products.html', context)

def detail_subcategory(request, subcategory_id):
	try:
		subcategory = SubCategory.objects.get(id=subcategory_id)
	except:
		raise Http404('Подкатегория не найдена!')

	context = {
		'subcategory': subcategory,
		'categories': Category.objects.filter(game=subcategory.category.game.id).order_by('name'),
		'subcategories': SubCategory.objects.filter(category=subcategory.category.id).order_by('-published'),
		'products': Product.objects.filter(subcategory=subcategory.id).order_by('-published'),
		'platforms': PlatForm.objects.filter(category_id=subcategory.category.id),
	}
	return render(request, 'home/detail_sub_category.html', context)

def search_product_subcategory(request, subcategory_id):
	try:
		subcategory = SubCategory.objects.get(id=subcategory_id)
	except:
		raise Http404('Тип товара не найден!')

	results = []
	if request.method == 'GET':
		query = request.GET.get('search')
		if query == '':
			queryset = None

	results = Product.objects.filter(Q(short_description__iregex=query), subcategory=subcategory_id).order_by('-published')
	context = {
		'subcategory': subcategory,
		'results': results,
		'query': query,
	}
	return render(request, 'home/search_products.html', context)

def create_product(request, category_id):
	try:
		category = Category.objects.get(id=category_id)
	except:
		raise Http404('Категория не найдена!')
	if request.method == 'POST':
		form = ProductForm(data=request.POST, category=category.id)
		form.instance.user = request.user
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ProductForm(category=category.id)
	context = {
		'form': form,
		'category': category,
	}
	return render(request, 'home/create_product.html', context)

def detail_category_game(request, category_id):
	try:
		categories = Category_Game.objects.get(id=category_id)
	except:
		raise Http404('Категория не найдена!')

	context = {
		'categories': categories,
		'category_games': Category_Game.objects.all().order_by(),
		'games': Game.objects.filter(category_game_id=categories.id),
	}
	return render(request, 'home/detail_category.html', context)

def detail_product(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except:
		raise Http404('Товар не найдена!')

	context = {
		'product': product,
		'products': Product.objects.filter(id=product_id),
		# 'platforms': PlatForms.objects.all(category_id=game_id),
	}
	return render(request, 'home/detail_product.html', context)

@login_required
def basket_list(request):
	context = {
		'baskets': Basket.objects.filter(user=request.user).order_by('-published'),
		'games': Game.objects.all(),
	}
	return render(request, 'home/baskets.html', context)

def basket_product_detail(request, product_id):
	try:
		basket = Basket.objects.get(id=product_id)
	except:
		raise Http404('Товар не найден!')

	context = {
		'basket': basket,
	}
	return render(request, 'home/basket_product_detail.html', context)

@login_required
def basket_add(request, product_id):
	Basket.create_or_update(product_id, request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
	basket = Basket.objects.get(id=basket_id)
	basket.delete()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def my_products_list(request):
	context = {
		'my_products_lists': Product.objects.filter(user=request.user).order_by('-published'),
		'games': Game.objects.all(),
	}
	return render(request, 'home/my_products_list.html', context)

def my_product_remove(request, product_id):
	product = Product.objects.get(id=product_id)
	product.delete()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def detail_currency(request, currency_id):
	try:
		currency = Category_Сurrency.objects.get(id=currency_id)
	except:
		raise Http404('Категория не найдена!')

	context = {
		'currency': currency,
		'currencies': Category_Сurrency.objects.filter(game=currency.game.id).order_by('name'),
		'categories': Category.objects.filter(game=currency.game.id).order_by('name'),
		'platForm_currencies': PlatForm_Currency.objects.filter(currency=currency.id).order_by('name'),
		'products_currencies': Product_Сurrency.objects.filter(currency_id=currency).order_by('-published'),
	}
	return render(request, 'home/detail_currency_products.html', context)

def detail_platform_currency(request, platform_currency_id):
	try:
		platform_currency = PlatForm_Currency.objects.get(id=platform_currency_id)
	except:
		raise Http404('Платформа не найдена!')

	context = {
		'platform_currency': platform_currency,
		'currencies': Category_Сurrency.objects.filter(game=platform_currency.currency.game.id).order_by('name'),
		'categories': Category.objects.filter(game=platform_currency.currency.game.id).order_by('name'),
		'platForm_currencies': PlatForm_Currency.objects.filter(currency=platform_currency.currency.id).order_by('name'),
		'products_currencies': Product_Сurrency.objects.filter(platform_currency=platform_currency.id).order_by('-published'),
	}
	return render(request, 'home/detail_platform_currency.html', context)

def create_product_currency(request, currency_id):
	try:
		currency = Category_Сurrency.objects.get(id=currency_id)
	except:
		raise Http404('Категория не найдена!')
	if request.method == 'POST':
		form = Product_СurrencyForm(data=request.POST, currency=currency.id)
		form.instance.user = request.user
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = Product_СurrencyForm(currency=currency.id)
	context = {
		'form': form,
		'currency': currency,
	}
	return render(request, 'home/create_product_currency.html', context)

def detail_product_currency(request, product_currency_id):
	try:
		product_currency = Product_Сurrency.objects.get(id=product_currency_id)
	except:
		raise Http404('Товар не найдена!')

	context = {
		'product_currency': product_currency,
		'products': Product_Сurrency.objects.filter(id=product_currency_id),
	}
	return render(request, 'home/detail_product_currency.html', context)

@login_required(login_url='/')
def my_purchase(request):
	purchases = Deal.objects.filter(user=request.user.id).order_by('-published')

	context = {
		'purchases': purchases,
		'number': [purchase for purchase in purchases],
	}
	return render(request, 'home/my_purchase.html', context)

@login_required(login_url='/')
def my_sell(request):
	sells = Deal.objects.filter(saleman=request.user.id).order_by('-published')

	context = {
		'sells': sells,
		'number': [sell for sell in sells],
	}
	return render(request, 'home/my_sells.html', context)

@login_required(login_url='/')
def deal_add(request, product_id):
	try:
		product = Product.objects.get(id=product_id)
	except:
		raise Http404('Товар не найден!')

	is_deal = Deal.objects.filter(short_description=product.short_description, price_for_1_piece=product.price_for_1_piece, user=request.user, saleman=product.user)
	if not is_deal.exists() is True:
		add_deal = Deal(short_description=product.short_description, price_for_1_piece=product.price_for_1_piece, user=request.user, saleman=product.user)
		add_deal.save()
	else:
		add_deal = Deal(short_description=product.short_description, price_for_1_piece=product.price_for_1_piece, user=request.user, saleman=product.user)
		add_deal.save()

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='/')
def deal_currency_add(request, product_currency_id):
	try:
		product_currency = Product_Сurrency.objects.get(id=product_currency_id)
	except:
		raise Http404('Товар не найден!')

	is_deal_currency = Deal_Currency.objects.filter(price_for_1_piece=product_currency.price_for_1_piece, currency=product_currency.currency, quantity=product_currency.availability, user=request.user, saleman=product_currency.user)
	if not is_deal_currency.exists() is True:
		add_deal_currency = Deal_Currency(price_for_1_piece=product_currency.price_for_1_piece, currency=product_currency.currency, quantity=product_currency.availability, user=request.user, saleman=product_currency.user)
		add_deal_currency.save()
	else:
		add_deal_currency = Deal_Currency(price_for_1_piece=product_currency.price_for_1_piece, currency=product_currency.currency, quantity=product_currency.availability, user=request.user, saleman=product_currency.user)
		add_deal_currency.save()

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='/')
def my_purchase_currency(request):
	purchases_currencies = Deal_Currency.objects.filter(user=request.user.id).order_by('-published')

	context = {
		# 'sell_currencies': Deal.objects.filter(purchase=request.user.id),
		'purchases_currencies': purchases_currencies,
		'number': [purchase_currency for purchase_currency in purchases_currencies],
	}
	return render(request, 'home/my_purchase_currency.html', context)

@login_required(login_url='/')
def my_sell_currency(request):
	sells_currencies = Deal_Currency.objects.filter(saleman=request.user.id).order_by('-published')

	context = {
		'sells_currencies': sells_currencies,
		'number': [sells_currency for sells_currency in sells_currencies],
	}
	return render(request, 'home/my_sell_currency.html', context)
