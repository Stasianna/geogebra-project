# Generated by Django 2.0.5 on 2018-05-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeogebraApplet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_file', models.FileField(upload_to='', verbose_name='Главный файл')),
            ],
        ),
    ]
