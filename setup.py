from distutils.core import setup

setup(
    name='relatedadminlink',
    version='0.0.1',
    author='Jonas Ohrstrom',
    author_email='ohrstrom@hazelfire.com',
    packages=['relatedadminlink',],
    #scripts=[],
    url='https://github.com/ohrstrom/django-relatedadminlink/',
    license='LICENSE.txt',
    description='Add links to related objects in django-admin.',
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.4.1",
    ],
)