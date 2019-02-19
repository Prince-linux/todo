# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField()),
                ('author', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
