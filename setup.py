import os

from setuptools import setup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='cp-external-login-egg',
    version='0.20.1',
    description='Django external authenticate method.',
    long_description=read('README.md'),
    author='CalipsoPlus',
    author_email='mis@cells.es',
    keywords="CalipsoPlus external login egg",
    url='http://www.calipsoplus.eu/',
    packages=['cp_authentication'],
    install_requires=['django==2.1.5', 'mysqlclient==1.4', 'djangorestframework==3.7.7'],
    classifiers=[
        "Development Status :: 1 - Planning",
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
