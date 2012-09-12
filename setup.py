from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 
    'Products', 'FSDExtender', 'version.txt')).read().strip()

setup(name='Products.FSDExtender',
    version=version,
    description="Extends the FSD to add additional fields",
    long_description=open("README.txt").read() + "\n" +
                     open("HISTORY.txt").read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='Chris Thomas',
    author_email='clt16@psu.edu',
    url='http://techsupport.la.psu.edu/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      'archetypes.schemaextender',
      # -*- Extra requirements: -*-
      ],
    entry_points="""
      # -*- Entry points: -*-
      """,
    )