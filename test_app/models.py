# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.db.models import Model, FileField, ImageField
from storagecellar import get_storage, NamedStorageFileField, \
    NamedStorageImageField


def a_file_storage():
    return get_storage('test_app.a_file.NonExistant')


class TestModel(Model):
    a_file = FileField(upload_to='a_file', null=True, storage=a_file_storage)
    an_image = ImageField(upload_to='an_image', null=True, storage=get_storage('test_app.an_image'))
    named_file = NamedStorageFileField(upload_to='named_file', null=True, storage='test_app.named_file')
    named_image = NamedStorageImageField(upload_to='named_image', null=True, storage='test_app.named_image')
    default_file = FileField(upload_to='a_file')
