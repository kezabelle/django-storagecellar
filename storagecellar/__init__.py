# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
from django.conf import settings
from django.core.files.storage import get_storage_class, default_storage
from django.db.models import FileField, ImageField
from django.utils import six


__version_info__ = '0.1.0'
__version__ = '0.1.0'
version = '0.1.0'
def get_version(): return version  # pragma: no cover


class recursive_itemgetter(object):
    """
    This was a couple of hours ago when I was going to have nested dicts ...
    """
    __slots__ = ('item', 'func')
    def __init__(self, item):
        self.item = item
        names = item.split('.')
        def func(obj):
            for name in names:
                try:
                    obj = obj[name]
                except LookupError:
                    # return the nearest up the chain
                    return obj
                except TypeError:
                    if not isinstance(obj, six.string_types):
                        six.reraise(*sys.exc_info())
                    return obj
            return obj
        self.func = func

    def __call__(self, obj):
        return self.func(obj)

    def __repr__(self):
        return '%s.%s(%s)' % (self.__class__.__module__,
                              self.__class__.__name__,
                              self.item)


def gen_keys(key):
    names = key.split('.')
    count = len(names)
    for x in xrange(count, 0, -1):
        yield '.'.join(names[0:x])


def get_storage(key):
    names = tuple(gen_keys(key))
    best_match = (settings.NAMEDSTORAGES[possible_name]
                  for possible_name in names
                  if possible_name in settings.NAMEDSTORAGES)
    name = next(best_match)
    # name = recursive_itemgetter(key)(settings.NAMEDSTORAGES)
    # if it's the same as the normal storage, avoid writing it to migrations...
    if name in (settings.DEFAULT_FILE_STORAGE, ''):
        return default_storage
    return get_storage_class(name)()



class NamedStorageFileField(FileField):
    def __init__(self, verbose_name=None, name=None, upload_to='',
                 storage='default', **kwargs):
        self._storage_name = storage
        storage = get_storage(self._storage_name)
        super(NamedStorageFileField, self).__init__(
            verbose_name=verbose_name, name=name, upload_to=upload_to,
            storage=storage, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(NamedStorageFileField, self).deconstruct()
        kwargs['storage'] = self._storage_name
        return name, path, args, kwargs


class NamedStorageImageField(ImageField):
    def __init__(self, verbose_name=None, name=None, width_field=None,
                 height_field=None, storage='default', **kwargs):
        self._storage_name = storage
        storage = get_storage(self._storage_name)
        super(NamedStorageImageField, self).__init__(
            verbose_name=verbose_name, name=name, width_field=width_field,
            height_field=height_field, storage=storage, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(NamedStorageImageField, self).deconstruct()
        kwargs['storage'] = self._storage_name
        return name, path, args, kwargs
