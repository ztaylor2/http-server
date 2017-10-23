"""The setup for mailroom project in python."""
from setuptools import setup

setup(
    name="http-server",
    description="Http server written in python",
    version=0.1,
    author="Zach Taylor & Jacob Carstens",
    author_email="zacharymtaylor3@gmail.com & <EMAIL>",
    license='MIT',
    py_modules=[],
    install_requires=['ipython'],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': []
    }
)
