from setuptools import setup
import sys,os

setup(
    name = 'shm-modbus-gui',
    version = '1.0.1',
    description = 'gui for shm-modbus',
    license='GPLv3',
    author = 'Nikolas Koesling',
    packages = [
        'src',
        'src.py_ui'
        ],
    package_data={},
    install_requires=['pyside6'],
    entry_points = {
        'console_scripts': [
            'shm-modbus-gui=src.main:main']
            },
    classifiers = ['Programming Language :: Python :: 3.10',
            'Operating System :: POSIX',
            'License :: GPLv3'],
)
