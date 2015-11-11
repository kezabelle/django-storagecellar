# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import test_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20151111_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='a_file',
            field=models.FileField(storage=test_app.models.a_file_storage, null=True, upload_to='a_file'),
        ),
    ]
