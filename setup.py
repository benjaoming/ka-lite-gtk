#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
#    'ka-lite',  # We do not have a way to specify ka-lite OR ka-lite-static
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ka-lite-gtk',
    version='0.1.0',
    description="User interface for KA Lite (GTK3)",
    long_description=readme + '\n\n' + history,
    author="Foundation for Learning Equality",
    author_email='info@learningequality.org',
    url='https://github.com/learningequality/ka-lite-gtk',
    packages=[
        'kalite_gtk',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='ka-lite-gtk, ka lite, ka-lite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'gui_scripts': [
            'ka-lite-gtk = kalite_gtk.__main__:main'
        ]
    },
)
