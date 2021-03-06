# coding: utf-8
from django.db import models

# Create your models here.

class Order(models.Model):
    email = models.CharField(max_length=256, verbose_name=u'E-mail')
    comment = models.TextField(verbose_name=u'Комментарий')

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'Заполнение формы отправки'
        verbose_name_plural = u'Заполнения формы отправки'

class MenuItem(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст страницы', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Разделы меню'
        verbose_name = u'Раздел меню'

class ImageItem(models.Model):
    image = models.ImageField(upload_to=u'upload/', verbose_name=u'Изображение', blank=True, null=True)
    small_image = models.ImageField(upload_to=u'upload/', verbose_name=u'Превью')
    menuitem = models.ForeignKey(MenuItem, verbose_name=u'Раздел меню')

    def __unicode__(self):
        return u'{}: {}'.format(self.menuitem.name, self.pk)

    class Meta:
        verbose_name_plural = u'Изображения'
        verbose_name = u'Изображение'