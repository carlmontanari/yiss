"""yiss.iosxr.bgp"""
import json

import xmltodict

from yiss.decorators import require_model


class BGP:
    @require_model
    def show_bgp_summary(
        self, full_output: bool = False, to_json: bool = False,
    ):
        """

        Args:
            full_output: return full xml output from netconf request before parsing
            to_json: return json output instead of dict

        Returns:
            resp: response as xml|json|dict

        RP/0/RP0/CPU0:abc1.sea99#show bgp summary
        Tue Dec 24 19:55:53.410 UTC
        BGP router identifier 172.32.254.254, local AS number 62985
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0xe0000000   RD version: 309297
        BGP main routing table version 309297
        BGP NSR Initial initsync version 635 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        BGP is operating in STANDALONE mode.


        Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
        Speaker          999999     999999     999999     999999      999999           0

        Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
        172.31.254.101    0 65535  999999  999999   999999    0    0     9w9d       9999
        172.31.254.102    0 65535  999999  999999   999999    0    0     9w9d       9999
        172.31.254.103    0 65535  999999  999999   999999    0    0     9d9h       9999
        172.31.254.104    0 65535  999999  999999   999999    0    0     9d9h       9999
        """
        resp = self.get(self.get_filter())

        if full_output:
            return resp
        resp = xmltodict.parse(resp.xml)
        resp = resp["rpc-reply"]["data"]["bgp"]["instances"]["instance"]["instance-active"][
            "default-vrf"
        ]["neighbors"]["neighbor"]

        if to_json:
            return json.dumps(resp)
        return resp
