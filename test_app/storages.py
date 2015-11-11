# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class StubStorage1(FileSystemStorage):
    def __init__(self):
        loc = os.path.join(settings.MEDIA_ROOT, '__stubstorage1')
        super(StubStorage1, self).__init__(location=loc)


class StubStorage2(FileSystemStorage):
    def __init__(self):
        loc = os.path.join(settings.MEDIA_ROOT, '__stubstorage2')
        super(StubStorage2, self).__init__(location=loc)
