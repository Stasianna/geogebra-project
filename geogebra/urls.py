from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from geogebra_applet.views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geogebra-applet/',
         include('geogebra_applet.urls', namespace='geogebra_applet')),
    path ('', MainPageView.as_view(), name='main_page'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]