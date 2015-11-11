# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include(admin.site.urls)),
]
