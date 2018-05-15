from django.views.generic import DetailView

from geogebra_applet.models import GeogebraApplet


class GeogebraAppletDetailView(DetailView):
    model = GeogebraApplet
