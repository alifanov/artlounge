from django.conf.urls import patterns, include, url

from app.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^design/$', DesignView.as_view(), name='design'),
    url(r'^mebel/$', MebelView.as_view(), name='mebel'),
    url(r'^art/$', ArtView.as_view(), name='art'),
    url(r'^order/$', OrderAjaxView.as_view(), name='order-ajax'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
