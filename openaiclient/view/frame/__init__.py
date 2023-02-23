# frame package __init__

# import all modules from package
from .baseframe import BaseFrame
from . import menuframe
from . import mainframe
from . import settings

# packages to import
__all__ = ["BaseFrame", "menuframe", "mainframe", "settings"]
