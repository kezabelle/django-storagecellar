# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import storagecellar


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20151111_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='named_file',
            field=storagecellar.NamedStorageFileField(storage='test_app.named_file', null=True, upload_to='named_file'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='named_image',
            field=storagecellar.NamedStorageImageField(storage='test_app.named_image', null=True, upload_to='named_image'),
        ),
    ]
