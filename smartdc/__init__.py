from .datacenter import *
from .machine import *
from .legacy import LegacyDataCenter

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
