from django.contrib import admin

from geogebra_applet.models import GeogebraApplet


@admin.register(GeogebraApplet)
class GeogebraAppletAdmin(admin.ModelAdmin):
    pass
