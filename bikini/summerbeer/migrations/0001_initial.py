# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('brewery', models.CharField(max_length=500)),
                ('brewery_website', models.URLField()),
                ('description', models.CharField(max_length=2000)),
                ('style', models.CharField(max_length=200)),
                ('abv', models.FloatField()),
                ('image', models.URLField(max_length=500)),
                ('review', models.CharField(max_length=2000)),
                ('hoppiness', models.FloatField()),
                ('drinkability', models.FloatField()),
                ('alldaybeer', models.FloatField()),
                ('fruitiness', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
