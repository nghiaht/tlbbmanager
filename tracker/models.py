# -*- coding: utf-8 -*-
from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=100)


class Item(models.Model):
    ITEM_TYPE_CHOICES = (
    ('TMTP', 'Tân mãng thần phù'),
    ('HBC', 'Hồn băng châu'),
    ('TTHHDTP', 'Trân thú huyễn hóa đan toái phiến'),
    ('NHT', 'Nhuận hồn thạch'),
    ('NGOC', 'Bảo thạch'),
    ('BT_YQ', 'Bí tịch, yếu quyết'),
    ('SCHTP', 'Sơ cấp hợp thành phù'),
    ('Toái phiến', 'Nguyên liệu toái phiến'),
    )

    account = models.ForeignKey(Account)
    name = models.CharField(max_length=50, verbose_name=u'Tên vật phẩm')
    type = models.CharField(max_length=100, choices=ITEM_TYPE_CHOICES, verbose_name=u'Loại vật phẩm')
    level = models.IntegerField(verbose_name=u'Cấp vật phẩm')
    quantity = models.IntegerField(verbose_name=u'Số lượng vật phẩm')



