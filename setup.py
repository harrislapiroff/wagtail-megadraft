from setuptools import setup, find_packages
from os import path
from wagtailmegadraft import __version__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='wagtail-megadraft',
    version=__version__,

    packages=find_packages(),
    include_package_data=True,

    description='A very nice rich content editor.',
    long_description=long_description,

    url='https://github.com/harrislapiroff/wagtail-megadraft',

    author='Harris Lapiroff',
    author_email='harris@chromamine.com',

    license='BSD-3-Clause',

    install_requires=[
        'wagtail>=2.3',
    ],

    extras_require={
        'docs': [
        ],
        'test': [
        ],
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 1',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
