from django.contrib import admin

from .models import Item, ShoppingCart, CustomUser
from django.contrib.auth.models import User

# Register your models here.


admin.site.register(User)
admin.site.register(ShoppingCart)
admin.site.register(CustomUser)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'count', 'author', 'genre', 'publish_date')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('author', 'genre', 'publish_date')