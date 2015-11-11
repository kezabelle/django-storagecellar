django-storagecellar 0.1.0
==========================

Someone mentioned wanting something vaguely like this on IRC. So let's go!

Define storages more like ``DATABASES`` or ``CACHES``::

    NAMEDSTORAGES = {
        'test_app': 'test_app.storages.StubStorage1',
        'default': 'django.core.files.storage.FileSystemStorage'
    }

Just a hack at the moment, untested. Migrations seemed to work though, which
is promising.

