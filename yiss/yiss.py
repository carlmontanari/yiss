"""yiss.yiss"""
from yiss.base import Base
from yiss.junos import JUNOS
from yiss.iosxe import IOSXE
from yiss.iosxr import IOSXR


DEVICES = {"default": Base, "junos": JUNOS, "iosxe": IOSXE, "iosxr": IOSXR}


class Device:
    def __new__(
        cls,
        host: str = "",
        port: int = 830,
        username: str = "",
        password: str = "",
        key: str = "",
        ssh_config: str = "",
        platform: str = "default",
        timeout: int = 30,
        model_version: str = "",
    ):
        """
        Initialize yiss Device object

        "Factory class" I guess -- a bit awkward but for if for no other reason than documentation
        this "feels" nicer than a factory function to me... fight me.

        Args:
            host: hostname/ip address of device
            port: port to connect on -- commonly 830 or 22
            username: username for connection
            password: password for given user (ignore if using keys)
            key: path to ssh key file for user
            ssh_config: path to ssh config file
            platform: device type -- default|junos|iosxe|iosxr
            timeout: timeout in seconds
            model_version: specific model version to use; follow yang model numbers; i.e. 662 for
                IOSXR version 6.6.2x; consult platform name/filters directory for supported
                versions/filters

        Returns:
            appropriate yiss Device object based on platform

        Raises:
            N/A  # noqa

        """
        if platform.lower() not in DEVICES:
            raise ValueError(f"Platform {platform} is invalid")

        connection_args = {}
        connection_args["host"] = host.strip()
        connection_args["port"] = port
        connection_args["username"] = username.strip()
        connection_args["device_params"] = {"name": platform.lower()}
        connection_args["timeout"] = timeout
        if key:
            connection_args["look_for_keys"] = True
            connection_args["hostkey_verify"] = False
            connection_args["key_filename"] = key
            connection_args["ssh_config"] = ssh_config
        else:
            connection_args["password"] = password

        kwargs = {}
        kwargs["model_version"] = model_version

        return DEVICES[connection_args["device_params"]["name"]](
            connection_args=connection_args, **kwargs
        )
