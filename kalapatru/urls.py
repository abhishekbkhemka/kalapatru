from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from kalapatru.views import home
from LR.views import (
    transporters,
    customers,
    forwardingNote,
    forwardingNotes,
    settings as api_settings,
    dispatch,
    dispatches,
    vans,
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/transporters/', transporters),
    path('api/forwardingNote/', forwardingNote),
    path('api/customers/', customers),
    path('api/settings/', api_settings),
    path('api/forwardingNotes/', forwardingNotes),
    path('api/dispatch/', dispatch),
    path('api/dispatches/', dispatches),
    path('api/vans/', vans),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
