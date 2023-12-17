from django.contrib import admin

from users.models import User, Country, Gender, BlackList

admin.site.register(BlackList)
admin.site.register(Gender)
admin.site.register(Country)
admin.site.register(User)
