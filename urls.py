from django.conf.urls.defaults import patterns
from core.views import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
  (r'^$', homepage),
)

urlpatterns += staticfiles_urlpatterns()

