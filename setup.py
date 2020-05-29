from setuptools import find_packages, setup

PACKAGE_NAME = 'tracking'
PACKAGE_VERSION = '0.1'
INSTALL_REQUIRES = [
    'pytest == 5.4.1',
    'requests == 2.23.0'
]

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='API testing for tracking packages between deposits',
    packages=find_packages(),
    python_requires='>=3.7.3',

    entry_points={
        'console_scripts': [
            'tracking = scripts.main:main'
        ]
    }
)
