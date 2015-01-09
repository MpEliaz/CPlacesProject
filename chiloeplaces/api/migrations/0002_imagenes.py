# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=300)),
                ('lugar', models.ForeignKey(to='api.Lugar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]