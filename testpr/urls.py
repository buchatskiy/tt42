from django.conf.urls import patterns, include, url
from users.views import main, edit_page, edit
from logreq.views import log_request
from django.conf import settings
from django.conf.urls.static import static
from loginsys.views import login, logout, register


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', main, {'htmlfile': 'base.html'}),
    url(r'^request/$', log_request, {'htmlfile': 'request.html'}),
    url(r'^edit/$', edit),
    url(r'^edit_page/$', edit_page, {'htmlfile': 'edit.html'}),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
