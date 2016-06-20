# -*- coding: utf-8 -*-


import os
from eve import Eve


this_dir = os.path.dirname(os.path.realpath(__file__))
settings_file = os.path.join(this_dir, 'settings.py')


def create_api():
    api = Eve(settings=settings_file)

    return api
