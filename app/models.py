# coding: utf-8
from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'Название')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Разделы меню'
        verbose_name = u'Раздел меню'

class ImageItem(models.Model):
    image = models.ImageField(upload_to=u'upload/', verbose_name=u'Изображение')
    small_image = models.ImageField(upload_to=u'upload/', verbose_name=u'Превью')
    menuitem = models.ForeignKey(MenuItem, verbose_name=u'Раздел меню')

    def __unicode__(self):
        return u'{}: {}'.format(self.menuitem.name, self.pk)

    class Meta:
        verbose_name_plural = u'Изображения'
        verbose_name = u'Изображение'