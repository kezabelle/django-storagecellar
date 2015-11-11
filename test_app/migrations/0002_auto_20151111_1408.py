# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import test_app.storages


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='a_file',
            field=models.FileField(storage=test_app.storages.StubStorage1(), null=True, upload_to='a_file'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='an_image',
            field=models.ImageField(storage=test_app.storages.StubStorage2(), null=True, upload_to='an_image'),
        ),
    ]
