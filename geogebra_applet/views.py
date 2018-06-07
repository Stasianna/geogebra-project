from django.views.generic import DetailView, CreateView, TemplateView

from geogebra_applet.models import GeogebraApplet


class GeogebraAppletDetailView(DetailView):
    model = GeogebraApplet

class MainPageView(TemplateView):
    template_name = 'geogebra_applet/main_str.html'
