import warnings

from yiss.base import Base
from yiss.iosxr.bgp import BGP
from yiss.iosxr.intf import INTF
from yiss.iosxr.isis import ISIS
from yiss.iosxr.mpls import MPLS


SUPPORTED_VERSIONS = ["662"]


class IOSXR(Base, BGP, INTF, ISIS, MPLS):
    def get_model_version(self):
        model_version = "".join(v[0] for v in self.version.split("."))
        if model_version not in SUPPORTED_VERSIONS:
            warnings.warn(
                f"Version {model_version} not in supported versions, picking nearest version!"
            )
            model_version = min(
                [int(v) for v in SUPPORTED_VERSIONS], key=lambda v: abs(v - int(model_version))
            )
        self.model_version = model_version
