# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.RemoveField(
            model_name='item',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='item',
            name='todo_list',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
