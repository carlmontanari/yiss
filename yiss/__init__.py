"""yiss network netconf library"""
import logging
from logging import NullHandler

from yiss.yiss import Device


__version__ = "2019.12.24"
__all__ = ("Device",)

# Setup logger
log = logging.getLogger(f"{__name__}")
logging.getLogger(f"{__name__}").addHandler(NullHandler())
