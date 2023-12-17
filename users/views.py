from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse, Http404
from django.contrib import auth

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User, BlackList
from home.models import Game, Product, Product_Сurrency, Review
# from chat.models import Message

def login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			email = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=email, password=password)
			if user:
				auth.login(request, user)
				return redirect('home')
	else:
		form = UserLoginForm()
	context = {
		'form': form,
	}
	return render(request, 'users/login.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('users:login')
	else:
		form = UserRegisterForm()
	context = {
		'form': form,
	}
	return render(request, 'users/register.html', context)

@login_required(login_url='/')
def profile(request, username):
	username = request.user
	user = User.objects.get(username=username)
	context = {
		'user': user,
		'games': Game.objects.all(),
		'reviews': Review.objects.filter(saleman=user.id).order_by('-published'),
	}
	return render(request, 'users/profile.html', context)

def logout(request):
	auth.logout(request)
	return redirect('home')

@login_required(login_url='/')
def settings_profile(request, username):
	username = request.user
	user = User.objects.get(username=username)
	if request.method == 'POST':
		form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('users:settings_profile', username.id)
		else:
			print(form.errors)
	else:
		form = UserProfileForm(instance=request.user)
	context = {
		'form': form,
		'user': user,
	}
	return render(request, 'users/settings_profile.html', context)

def user_account(request, account_id):
	try:
		other_user = User.objects.get(id=account_id)
	except:
		raise Http404('Пользователь не найден!')

	message = User.objects.get(id=account_id)
	#message_self = Message.objects.get(id=account_id)
	context = {
		'other_user': other_user,
		'products': Product.objects.filter(user=other_user.id).order_by('-published'),
		'products_currencies': Product_Сurrency.objects.filter(user=other_user.id).order_by('-published'),
		'reviews': Review.objects.filter(saleman=other_user.id).order_by('-published'),
		'message': message,
		#'message_self': message_self,
	}
	return render(request, 'users/another_user_profile.html', context)

def blacklist(request):
	context = {
		'bans': BlackList.objects.filter(banned_user=request.user.id),
	}
	return render(request, 'users/ban.html', context)

