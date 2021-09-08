from django.contrib import admin
from .models import Category, Item, PictureItem


class PictureItemInline(admin.TabularInline):
    model = PictureItem
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created',)
    inlines = [
        PictureItemInline,
    ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
