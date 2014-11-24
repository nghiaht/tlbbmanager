# -*- coding: utf-8 -*-
from django.db import models

class Account(models.Model):
    character_name = models.CharField(max_length=25, verbose_name=u'Tên nhân vật')
    username = models.CharField(max_length=30, verbose_name=u'Tên tài khoản')
    password = models.CharField(max_length=50, verbose_name=u'Mật khẩu')
    role = models.CharField(max_length=100, verbose_name=u'Vai trò')
    energy_points = models.IntegerField(default=0, verbose_name='Điểm hoạt động')
    #items = models.ManyToManyField('Item', db_constraint=False)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'Tài khoản'
        verbose_name_plural = u'Tài khoản'

class ItemType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name=u'Tên loại vật phẩm')
    short_type_name = models.CharField(max_length=15, verbose_name=u'Viết tắt loại vật phẩm', null=True, blank=True)

    def __unicode__(self):
        return '%s - %s' % (self.short_type_name, self.type_name)

    class Meta:
        verbose_name = u'Loại vật phẩm'
        verbose_name_plural = u'Loại vật phẩm'

class Item(models.Model):
    # ITEM_TYPE_CHOICES = (
    # ('TMTP', 'Tân mãng thần phù'),
    # ('HBC', 'Hồn băng châu'),
    # ('TTHHDTP', 'Trân thú huyễn hóa đan toái phiến'),
    # ('NHT', 'Nhuận hồn thạch'),
    # ('NGOC', 'Bảo thạch'),
    # ('BT_YQ', 'Bí tịch, yếu quyết'),
    # ('SCHTP', 'Sơ cấp hợp thành phù'),
    # ('Toái phiến', 'Nguyên liệu toái phiến'),
    # )

    #account = models.ForeignKey(Account, verbose_name=u'Tài khoản', db_constraint=False)
    name = models.CharField(max_length=50, verbose_name=u'Tên vật phẩm', null=True, blank=True)
    #type = models.CharField(max_length=100, choices=ITEM_TYPE_CHOICES, verbose_name=u'Loại vật phẩm', null=True, blank=True)
    type = models.ForeignKey(ItemType, verbose_name=u'Loại vật phẩm', null=True, db_constraint=False)
    level = models.IntegerField(verbose_name=u'Cấp vật phẩm', null=True, default=0)

    def __unicode__(self):
        return '%s - %s %s' % (self.name, '' if not self.type else self.type, '' if self.level == 0 else self.level)

    class Meta:
        verbose_name = u'Vật phẩm'
        verbose_name_plural = u'Vật phẩm'


class ItemDetail(models.Model):
    item = models.ForeignKey(Item, verbose_name=u'Vật phẩm', db_constraint=False)
    account = models.ForeignKey(Account, verbose_name=u'Tài khoản', db_constraint=False)
    quantity = models.IntegerField(verbose_name=u'Số lượng vật phẩm', default=0, null=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.item, '' if self.quantity == 0 else 'x' + str(self.quantity) )


    class Meta:
        verbose_name = u'Chi tiết vật phẩm'
        verbose_name_plural = u'Chi tiết vật phẩm'