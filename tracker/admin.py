# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class ItemInline(admin.TabularInline):
    model = Item

class ItemDetailInline(admin.TabularInline):
    model = ItemDetail

class AccountAdmin(admin.ModelAdmin):
    inlines = [ItemDetailInline]
    list_display = ['character_name', 'username', 'password', 'role', 'energy_points']
#
#

class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ['item', 'account', 'quantity']

admin.site.register(Account, AccountAdmin)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(ItemDetail, ItemDetailAdmin)