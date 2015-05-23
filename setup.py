from distutils.core import setup
from setuptools import find_packages

setup(
    name='Django Pipline Helpers',
    version="0.1.0",
    author='Jason Goldstein',
    author_email='jason@betheshoe.com',
    url='https://bitbucket.org/whatisjasongoldstein/django-pipeline-helpers',
    packages=find_packages(),
    include_package_data=True,
    description='For keeping static files out for settings.py',
    long_description=open('README.markdown').read(),
)