import os

from setuptools import setup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='calipso-plugin-db-authentication',
    version='1.20.4',
    description='Django external authenticate method.',
    long_description=read('README.md'),
    author='CalipsoPlus',
    author_email='mis@cells.es',
    keywords="CalipsoPlus external login egg",
    url='http://www.calipsoplus.eu/',
    packages=[
        'cp_authentication',
        'cp_authentication.auth',
        'cp_authentication.migrations',
        'cp_authentication.models',
        'cp_authentication.templates',
        'cp_authentication.views'],
    install_requires=['django', 'mysqlclient', 'djangorestframework'],
    classifiers=[
        "Development Status :: 1 - Planning",
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
