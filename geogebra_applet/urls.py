from django.urls import path

from geogebra_applet.views import GeogebraAppletDetailView

app_name = 'geogebra_applet'

urlpatterns = [
    path('<int:pk>/', GeogebraAppletDetailView.as_view(), name='detail'),
]
