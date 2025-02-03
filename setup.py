# Silly commands:
# python setup.py bdist bdist_wheel
# twine upload dist/*
from setuptools import setup, find_packages


with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name="pyritofile",
    version="0.2.1",
    
    author="GuiSaiUwU",
    author_email="contaguardian@gmail.com",
    url="https://github.com/GuiSaiUwU/pyritofile-package",
    description="Python package to deal with League of Legends files.",
    
    packages=find_packages(),
    install_requires=[
        "xxhash>=3.5.0",
        "pyzstd>=0.16.2"
    ],
    long_description_content_type='text/markdown',
    long_description=long_description,
    
    license="GPLv3+"
)