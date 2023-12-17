from django import forms

from home.models import Product, Category, Game, PlatForm, SubCategory, Product_Сurrency, PlatForm_Currency, Category_Сurrency

class ProductForm(forms.ModelForm):
	short_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	price_for_1_piece = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	availability = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}))
	category = forms.ModelChoiceField(queryset=Category.objects.filter(), empty_label='Категория', widget=forms.Select(attrs={'class': 'form-control'},))
	platform = forms.ModelChoiceField(queryset=PlatForm.objects.filter(), empty_label='Платформа', widget=forms.Select(attrs={'class': 'form-control'},))
	subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.filter(), empty_label='Тип товара', widget=forms.Select(attrs={'class': 'form-control'},))
	game = forms.ModelChoiceField(queryset=Game.objects.filter(), empty_label='Игра', widget=forms.Select(attrs={'class': 'form-control'},))

	class Meta:
		model = Product
		fields = ('short_description', 'description', 'price_for_1_piece', 'image', 'availability', 'category', 'platform', 'subcategory', 'game')

	def __init__(self, category, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['game'].queryset = Game.objects.filter(category=category)
		self.fields['category'].queryset = Category.objects.filter(id=category)
		self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category)
		self.fields['platform'].queryset = PlatForm.objects.filter(category=category)

class Product_СurrencyForm(forms.ModelForm):
	price_for_1_piece = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	availability = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0'}))
	platform_currency = forms.ModelChoiceField(queryset=PlatForm_Currency.objects.filter(), empty_label='Платформа', widget=forms.Select(attrs={'class': 'form-control'},))
	game = forms.ModelChoiceField(queryset=Game.objects.filter(), empty_label='Игра', widget=forms.Select(attrs={'class': 'form-control'},))
	currency = forms.ModelChoiceField(queryset=Category_Сurrency.objects.filter(), empty_label='Категория', widget=forms.Select(attrs={'class': 'form-control'},))
	
	class Meta:
		model = Product_Сurrency
		fields = ('price_for_1_piece', 'availability', 'platform_currency', 'game', 'image', 'currency',)

	def __init__(self, currency, *args, **kwargs):
		super(Product_СurrencyForm, self).__init__(*args, **kwargs)
		self.fields['game'].queryset = Game.objects.filter(id=currency)
		self.fields['currency'].queryset = Category_Сurrency.objects.filter(id=currency)
		self.fields['platform_currency'].queryset = PlatForm_Currency.objects.filter(currency_id=currency)
