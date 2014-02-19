# -*- coding: utf-8 -*-
"""
    setup.py
    ~~~~~~~~

    :copyright: (c) 2014, swtstore authors. see AUTHORS file for more details.
    :license: BSD License, see LICENSE for more details.
"""

"""
swtstore
--------

The sweet store for decentralized, semantic, social web tweets a.k.a SWeeTs!!

"""
from setuptools import setup

requires = [
    'Flask',
    'Flask-SQLAlchemy',
    'sqlalchemy'
]


setup(
    name='swtstore',
    version='0.1 - alpha',
    url='https://git.pantoto.org/sweet-web',
    license='BSD',
    author='Halwai',
    author_email='rayanon@servelots.com',
    description='Server-side store for decentralized, semantic, social, web\
                tweets',
    long_description=__doc__,
    packages=['swtstore'],
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Social :: Semantic :: Decentralized',
    ]
)