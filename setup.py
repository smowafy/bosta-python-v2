from setuptools import setup

setup(
    name='Bosta',
    version='1.0.0',
    author='bosta',
    author_email='sdk@bosta.com',
    scripts=[],
    keywords=["bosta", "client-sdk", "api", "api-integration"],
    url='http://pypi.python.org/pypi/bosta/',
    license='LICENSE',
    description='Bosta Python SDK',
    long_description=open('README.md').read(),
    install_requires=[
        'requests'
    ],
)
