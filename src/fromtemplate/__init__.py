"""
__init__.py

This file initializes the package and defines the package's version.
"""

# read version from installed package
from importlib.metadata import version

__version__ = version(__name__)
