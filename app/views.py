# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import *
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class DesignView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(DesignView, self).get_context_data(**kwargs)
        ctx['photos'] = ImageItem.objects.filter(menuitem__name=u'Дизайн и декор')
        ctx['text'] = MenuItem.objects.get(name=u'Дизайн и декор').text
        return ctx

class MebelView(TemplateView):
    template_name = 'gallery.html'

class ArtView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArtView, self).get_context_data(**kwargs)
        ctx['photos'] = ImageItem.objects.filter(menuitem__name=u'Искусство')
        ctx['text'] = MenuItem.objects.get(name=u'Искусство').text
        return ctx
