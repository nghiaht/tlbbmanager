# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class ItemInline(admin.TabularInline):
    model = Item


class AccountAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

#
#
admin.site.register(Account, AccountAdmin)
