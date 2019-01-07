"""
# setup module
"""

import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

BASE = 'jinchi/' if os.path.isdir(os.path.join(HERE, 'jinchi')) else ''

PREQ = os.path.join(HERE, BASE + "requirements.txt")
PREQ_DEV = os.path.join(HERE, BASE + "requirements-dev.txt")

setup(
    name='jinchi',
    version='0.0.1',
    description='Coding demo for Python',
    long_description=README + '\n\n' + CHANGES,
    classifiers=["Programming Language :: Python",
                 "Topic :: Internet :: Demo"],
    author='Jinchi Zhang',
    author_email='jizjiz148148@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=PREQ,
    tests_require=PREQ_DEV,
    test_suite="jinchi",
    entry_points="""\
    [paste.app_factory]
    main = jinchi:main
    """,
)
