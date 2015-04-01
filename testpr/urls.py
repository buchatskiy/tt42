from django.conf.urls import patterns, include, url
from users.views import main


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', main, {'htmlfile': 'base.html'}),
    url(r'^admin/', include(admin.site.urls)),
)
