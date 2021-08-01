from setuptools import setup
from setuptools import find_packages


Name = 'weather-service-backend'
Author = 'Napo Limited'
AuthorEmail = ''
Maintainer = 'Napo Limited'
Summary = 'Backend Developer Pair-programming test.'
License = 'All rights reserved'
with open('VERSION') as fd:
    Version = fd.read().strip()
Description = Summary
ShortDescription = Summary

with open('requirements.txt') as fd:
    install_requires = fd.readlines()


setup(
    name=Name,
    zip_safe=False,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=Summary,
    long_description=Description,
    classifiers=["Programming Language :: Python"],
    license=License,
    include_package_data=True,
    install_requires=install_requires,
    packages=find_packages(),
)
