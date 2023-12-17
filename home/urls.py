from django.urls import path

from home.views import role, my_sell_currency, my_sell, my_purchase_currency, deal_currency_add, my_purchase, deal_add, detail_product_currency, create_product_currency, detail_platform_currency, detail_currency, search_product_game, search_game, search_product_subcategory, search_product_category, search_product_platform, detail_subcategory, detail_platform, detail_game, detail_category, create_product, search_by_games, detail_category_game, detail_product, basket_add, basket_list, basket_remove, basket_product_detail, my_products_list, my_product_remove

app_name = 'home'

urlpatterns = [
	path('orders/sell/currency/', my_sell_currency, name='my_sell_currency'),
	path('orders/sell/', my_sell, name='my_sells'),
	path('orders/currency/', my_purchase_currency, name='my_purchase_currency'),
	path('order_currency_add/<int:product_currency_id>/', deal_currency_add, name='purchase_currency_add'),
	path('deal_add/<int:product_id>/', deal_add, name='deal_add'),
	path('orders/', my_purchase, name='my_purchase'),
	path('product_currency/<int:product_currency_id>/', detail_product_currency, name='detail_product_currency'),
	path('currency/<int:currency_id>/add/item/', create_product_currency, name='create_product_currency'),
	path('currency/platform_currency/<int:platform_currency_id>/', detail_platform_currency, name='detail_platform_currency'),
	path('currency/<int:currency_id>/', detail_currency, name='detail_currency_products'),
	path('category/product_type/<int:subcategory_id>/search_product/', search_product_subcategory, name='search_product_in_subcategory'),
	path('category/<int:category_id>/search_product/', search_product_category, name='search_product_in_category'),
	path('category/platform/<int:platform_id>/search_product/', search_product_platform, name='search_product_in_platform'),
	path('game/<int:game_id>/search_product/', search_product_game, name='search_product'),
	path('search_game/', search_game, name='search_game'),
	path('category/product_type/<int:subcategory_id>/', detail_subcategory, name='detail_subcategory'),
	path('category/platform/<int:platform_id>/', detail_platform, name='detail_platform'),
	path('product_remove/<int:product_id>/', my_product_remove, name='my_product_remove'),
	path('my_products_list/', my_products_list, name='my_products_list'),
	path('basket_products/<int:product_id>/detail_item/', basket_product_detail, name='basket_product_detail'),
	path('basket_products/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
	path('basket_products/', basket_list, name='basket_list'),
	path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
	path('detail_products/<int:product_id>/', detail_product, name='detail_product'),
	path('category_game/<int:category_id>/', detail_category_game, name='detail_category_game'),
	path('search_by_games/', search_by_games, name='search_by_games'),
	path('category/<int:category_id>/add/item/', create_product, name='create_product'),
	path('category/<int:category_id>/', detail_category, name='detail_category_products'),
	path('deal/info/', role, name='role'),
	path('game/<int:game_id>/', detail_game, name='detail_game'),
]
