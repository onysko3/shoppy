from django.contrib import admin
from .models import Category, Item




class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
