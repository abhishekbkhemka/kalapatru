from django.conf.urls import patterns, include, url
from django.contrib import admin
from LR.views import transporters,customers,forwardingNote,forwardingNotes,settings,dispatch,dispatches,vans
from model_report.urls import *
from model_report import report
from stock.views import stock

report.autodiscover()
admin.autodiscover()
print admin.site.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kalapatru.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # url(r'', include('model_report.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/transporters/$', transporters),
    url(r'^api/forwardingNote/$', forwardingNote),
    url(r'^api/customers/$', customers),
    url(r'^api/settings/$', settings),
    url(r'^api/forwardingNotes/$', forwardingNotes),
    url(r'^api/dispatch/$', dispatch),
    url(r'^api/dispatches/$', dispatches),
    url(r'^api/vans/$', vans),
    url(r'^report/', include('model_report.urls')),
    url(r'^stock/', stock),
)
