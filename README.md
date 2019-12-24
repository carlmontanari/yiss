[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

yiss: YANG is Super Shitty
=======

At the moment I do not have strong feelings of love for YANG, which may be evident by the name of this repo! YISS gathers the same output as some show commands that are used frequently in my environment, but does so via NETCONF/YANG. Is this any better than using SSH and TextFSM? I don't particularly think so -- the reliability of SSH/TextFSM is probably just as high or higher than relying on models that could (just like SSH output) change without my noticing. In any case YISS is my little shim so I can say that I'm using NETCONF/YANG but only have to write it once, then I can just deal with XML/JSON/dicts to pull out the bits of information I care about.

TL;DR -- YISS is a wrapper around ncclient that let's you fire up a NETCONF connection to a device and then simply call methods that map to known cli commands, such as `show interface` or `show ip bgp summary`.
 
# Platforms

At the moment only IOS-XR has any real support and its likely to stay that way; though in theory IOS-XE, Junos, and others could easily be shoe horned into YISS.  