from setuptools import setup

setup(
   name='Bosta',
   version='0.1.0',
   author='bosta',
   author_email='sdk@bosta.com',
   scripts=[],
   url='http://pypi.python.org/pypi/bosta/',
   license='LICENSE.txt',
   description='Bosta Python SDK',
   long_description=open('README.txt').read(),
   install_requires=[
       'requests'
   ],
)