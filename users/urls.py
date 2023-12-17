from django.urls import path

from users.views import login, register, profile, logout, settings_profile, user_account, blacklist

app_name = 'users'

urlpatterns = [
	path('ban/', blacklist, name='ban'),
	path('id/<int:account_id>/', user_account, name='user_account'),
	# path('ids/<int:account_id>/', user_account_currency, name='user_account_currency'),
	path('settings_profile/<int:username>/', settings_profile, name='settings_profile'),
	path('logout/', logout, name='logout'),
	path('login/', login, name='login'),
	path('registration/', register, name='register'),
	path('profile/<int:username>/', profile, name='profile'),
]