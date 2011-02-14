#!/usr/bin/env python
import os

from setuptools import setup, find_packages

from makesite import VERSION, PROJECT, LICENSE


PACKAGE_DATA = [ '*.ini' ]

for folder in ['base', 'templates', 'modules']:
    for root, dirs, files in os.walk(os.path.join(PROJECT, folder)):
        for filename in files:
            PACKAGE_DATA.append("%s/%s" % ( root[len(PROJECT)+1:], filename ))


def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''


META_DATA = dict(
    name=PROJECT,
    version=VERSION,
    license=LICENSE,
    description=read( 'DESCRIPTION' ),
    long_description=read( 'README.rst' ),
    platforms=('Any'),

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url=' http://github.com/klen/makesite',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Environment :: Console',
        'Topic :: Software Development :: Code Generators',
    ],

    packages=find_packages(),
    scripts=map( lambda x: 'scripts/' + x, os.listdir( 'scripts' )),
    package_data = { '': PACKAGE_DATA, },

    entry_points={
        'console_scripts': [
            'makesite = makesite.main:main',
        ]
    },
)


if __name__ == "__main__":
    setup( **META_DATA )
