# -*- coding: utf-8 -*-

import click
import os
from . import factory

@click.group()
def main(args=None):
    """Console script for api"""
    pass
    
@main.command()
@click.option('--host')
@click.option('--port', type=int)
def run(host=None, port=None):
    if host is None:
        host = os.environ.get('HOST', '0.0.0.0')

    if port is None:
        port = int(os.environ.get('PORT', 5000))

    api = factory.create_api()
    api.run(host=host, port=port)

if __name__ == "__main__":
    main()
