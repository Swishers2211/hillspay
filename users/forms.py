from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User, Country, Gender

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

	class Meta:
		model = User
		fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
	country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('country'), empty_label='Выберите страну', widget=forms.Select(attrs={'class': 'form-control',},))
	gender = forms.ModelChoiceField(queryset=Gender.objects.all(), empty_label='Выберите пол', widget=forms.Select(attrs={'class': 'form-control'},))

	class Meta:
		model = User
		fields = ('image', 'username', 'email', 'country', 'gender',)
