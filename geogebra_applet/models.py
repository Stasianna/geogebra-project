import os
from zipfile import ZipFile

from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import ugettext_lazy as _


def generate_file_name(instance, filename):
    return os.path.join('geogebra_applet/', filename)


class GeogebraApplet(models.Model):
    archive = models.FileField(
        _("Архив"),
        upload_to='geogebra_applet',
        null=True
    )
    index_file = models.FileField(
        _("Главный файл"),
        upload_to=generate_file_name,
        blank=True
    )

    def save(self, **kwargs):
        super().save(**kwargs)
        if self.index_file:
            return
        path = self.archive.path.split('.')[0]
        if not os.path.exists(path):
            os.mkdir(path)
        with ZipFile(self.archive.path, 'r') as archive:
            archive.extractall(path=path)
        for filename in os.listdir(path):
            if filename.split('.')[-1] == 'html':
                path_to_html = os.path.join(path, filename)
                f = open(path_to_html, 'rb')
                cont = f.read()
                new_filename = os.path.join(os.path.split(path)[-1], filename)
                self.index_file.save(new_filename, ContentFile(cont), save=False)
                f.close()
        super().save(**kwargs)


