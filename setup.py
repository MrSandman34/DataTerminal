import sys
from setuptools import setup
sys.setrecursionlimit(1000000)

DATA_FILES = []
OPTIONS ={'packages': 'certifi'}

setup(
    app=['DataTerminal.py'],
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app']
)
