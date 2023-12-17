from django.contrib import admin

from home.models import Role, Review, Deal_Currency, Deal, PlatForm_Currency, Category, Game, SubCategory, Product, PlatForm, Category_Game, Basket, Product_Сurrency, Category_Сurrency

admin.site.register(Role)
admin.site.register(Review)
admin.site.register(Deal)
admin.site.register(Deal_Currency)
admin.site.register(PlatForm_Currency)
admin.site.register(Category_Сurrency)
admin.site.register(Product_Сurrency)
admin.site.register(Basket)
admin.site.register(Category_Game)
admin.site.register(PlatForm)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Game)
