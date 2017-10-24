
import os

from setuptools import setup

setup (
    name='SimAnalysisTools',
    version='1.0.0',
    description='Tools to analyze molecular simulations',
    long_description=open('README.md').read(),
    url='https://github.com/sgenheden/SimAnalysisTools',
    author='Samuel Genheden',
    author_email='samuel.genheden@gmail.com',
    license='MIT',

    packages=['simanalysis',],
    entry_points={'console_scripts': ['simanalysis = simanalysis.tools:simanal', ]},
    install_requires=['numpy','MDAnalysis','scikit-learn'],
)
