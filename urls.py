from django.conf.urls.defaults import patterns, include, url
from core.views import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', homepage, {'template': 'index.html'}),
  (r'^inscricao/', include('subscription.urls', namespace='subscription')),
  (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
