import io
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='python-workshop',
    version='1.0.0',
    author='Harvard NRG',
    author_email='info@neuroinfo.org',
    description='Python workshop materials.',
    url='https://github.com/harvard-nrg/python-workshop',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    license='BSD-3-Clause',
    packages=find_packages(),
    include_package_data=True,
    install_requires=io.open('requirements.txt').read().splitlines(),
    scripts=[]
)
