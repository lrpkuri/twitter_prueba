"""Cotizador URLs."""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(
        '',
        include(
            'useraccounts.urls',
            namespace='useraccounts'
        ),
    ),
    url(
        r'^tuits/',
        include(
            'tuiti.urls',
            namespace='tuiti'
        ),
    ),
    url(
        r'^admin/', admin.site.urls
    ),
    url(
        '^',
        include(
            'django.contrib.auth.urls'
            )
        )
]
