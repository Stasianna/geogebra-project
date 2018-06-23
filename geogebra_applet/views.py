#from django.http import HttpResponse
#from django.http import response_redirect
from django.shortcuts import render_to_response
from django.views.generic import DetailView, CreateView, TemplateView

from geogebra_applet.models import GeogebraApplet


class GeogebraAppletDetailView(DetailView):
    model = GeogebraApplet

class MainPageView(TemplateView):
    template_name = 'geogebra_applet/main_str.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['arhives'] = GeogebraApplet.objects.all()
        return context

def ViewHtml(request, file):
    copymodel = GeogebraApplet.objects.filter(id = file).first()
    f = copymodel.index_file.open(mode="rb")
    return render_to_response(copymodel.index_file.url)

