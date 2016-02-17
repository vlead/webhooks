
from setuptools import setup

requires = [
    'flask',
    'flask-cors',
    'flask-testing',
    'requests'
]

setup(
    name='webhooks',
    version='0.1',
    install_requires=requires
)
