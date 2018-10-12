# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('DNI', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
                ('fecha_nac', models.DateTimeField(null=True, blank=True)),
                ('fechaalta', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
