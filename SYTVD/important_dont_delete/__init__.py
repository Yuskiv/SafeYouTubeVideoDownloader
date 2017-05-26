#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
__title__ = 'important_dont_delete'
__version__ = '6.2.2'
__author__ = 'Pavlo Yuskiv'

from .api import YouTube

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
