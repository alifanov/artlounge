# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.core.mail import send_mail
import django_settings
# Create your views here.

class GeneralMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(GeneralMixin, self).get_context_data(**kwargs)
        ctx['order_form'] = OrderForm()
        return ctx

class OrderAjaxView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save()
                msg = u'E-mail: {}\nКомментарий: {}'.format(order.email, order.comment)
                send_mail(u'Заполнение формы на сайте art-lounge.ru',msg, 'info@art-lounge.ru', [django_settings.get('admin_email'),])
        return HttpResponse('OK')

class HomeView(GeneralMixin, TemplateView):
    template_name = 'home.html'

class DesignView(GeneralMixin, TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(DesignView, self).get_context_data(**kwargs)
        ctx['photos'] = ImageItem.objects.filter(menuitem__name=u'Дизайн и декор')
        ctx['text'] = MenuItem.objects.get(name=u'Дизайн и декор').text
        ctx['active'] = 'design'
        return ctx

class MebelView(GeneralMixin, TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(MebelView, self).get_context_data(**kwargs)
        ctx['photos'] = ImageItem.objects.filter(menuitem__name=u'Мебель')
        ctx['text'] = MenuItem.objects.get(name=u'Мебель').text
        ctx['active'] = 'mebel'
        return ctx

class ArtView(GeneralMixin, TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArtView, self).get_context_data(**kwargs)
        ctx['photos'] = ImageItem.objects.filter(menuitem__name=u'Искусство')
        ctx['text'] = MenuItem.objects.get(name=u'Искусство').text
        ctx['active'] = 'art'
        return ctx
