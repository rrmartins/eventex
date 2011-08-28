from django.conf.urls.defaults import patterns, url
from route import route
from subscription.views import subscribe
     
urlpatterns = patterns('subscription.views',
    route(r'^$', GET='new', POST='create', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)


