"""yiss.base"""
from pathlib import Path
import sys

from lxml import etree
from ncclient import manager

import yiss


class Base:
    def __init__(self, connection_args: dict, model_version: str = ""):
        """
        Initialize Base yiss object

        Args:
            connection_args: dictionary of connection arguments; see yiss.Device
            model_version: string of model version to use; set as "none" to ignore model
                specific methods

        Returns:
            N/A  # noqa

        Raises:
            N/A  # noqa

        """
        self.platform = connection_args["device_params"]["name"]
        self.platform_filts = f"{Path(yiss.__file__).parents[0]}/{self.platform}/filters"
        self.timeout = connection_args.pop("timeout")
        self.connection_args = connection_args

        self.version = None
        self.model_version = model_version
        self.conn = None

    def _get_filter(self):
        """
        Private method to get filter based on platform, model version and method name

        Args:
            N/A  # noqa

        Returns:
            N/A  # noqa

        Raises:
            N/A  # noqa

        """
        with open(
            f"{self.platform_filts}/{self.model_version}/{sys._getframe(1).f_code.co_name}.xml"  # noqa
        ) as f:
            return f.read()

    def open(self):
        """
        Open netconf connection to device

        Args:
            N/A  # noqa

        Returns:
            N/A  # noqa

        Raises:
            N/A  # noqa

        """
        self.conn = manager.connect(**self.connection_args)
        self.conn.timeout = self.timeout
        if self.model_version.lower() == "none":
            self.model_version = None
        elif not self.model_version:
            if any(
                "http://openconfig.net/yang/platform" in c for c in self.conn.server_capabilities
            ):
                self.get_version()
                self.get_model_version()
            else:
                self.model_version = None

    def close(self):
        """
        Close netconf connection to device

        Args:
            N/A  # noqa

        Returns:
            N/A  # noqa

        Raises:
            N/A  # noqa

        """
        self.conn.close_session()

    def get_version(self):
        """
        Get version using openconfig/platform yang model

        Args:
            N/A  # noqa

        Returns:
            N/A  # noqa

        Raises:
            N/A  # noqa

        """
        # could/should be overriden by platform specific version stuff
        with open(f"{Path(yiss.__file__).parents[0]}/filters/version.xml") as f:
            filt = f.read()
        resp = self.get(filt)
        tree = etree.fromstring(resp.xml)
        vers = tree.xpath(
            "//ns:software-version", namespaces={"ns": "http://openconfig.net/yang/platform"},
        )
        # hack that assumes that versions will just show up in all elements of this xpath search
        # tested only on iosxr 662, no idea if this works on junos or iosxe
        self.version = vers[0].text

    def get_model_version(self):
        """
        Get model version based on software version

        Args:
            N/A  # noqa

        Returns:
            N/A  # noqa

        Raises:
            N/A  # noqa

        """
        self.model_version = self.version

    def get_config(self, source: str = "running", filt: str = ""):
        """
        Get configuration using ncclient get_config

        Args:
            source: running|startup|candidate -- possibly other options?
            filt: xml filter to apply to get_config call

        Returns:
            configuration received from device

        Raises:
            N/A  # noqa

        """
        return self.conn.get_config(source, filt)

    def get(self, filt: str = ""):
        """
        Get operational data using ncclient get

        Args:
            filt: xml filter to apply to get_config call

        Returns:
            operational data received from device

        Raises:
            N/A  # noqa

        """
        return self.conn.get(filt)
