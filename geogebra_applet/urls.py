from django.urls import path

from geogebra_applet.views import GeogebraAppletDetailView

app_name = 'geogebra_applet'

urlpatterns = [
    path('<int:pk>/', GeogebraAppletDetailView.as_view(), name='detail'),
]


#from django.urls import path, include

#from geogebra_applet.views import GeogebraAppletDetailView, MainPageView

#app_name = 'geogebra_applet'

#urlpatterns = [
#    path('<int:pk>/', GeogebraAppletDetailView.as_view(), name='detail'),
#    path('geogebra-applet/',
 #        include('geogebra_applet.urls',namespace='geogebra_applet')),
 #   path ('', MainPageView.as_view(), name='main_page'),
 #   path('View/<int:file>', ViewHtml, name='detail'),
#]

#if settings.DEBUG:
 #   urlpatterns += [
 #       re_path(r'^media/(?P<path>.*)$', serve, {
 #           'document_root': settings.MEDIA_ROOT,
 #       }),
 #   ]
