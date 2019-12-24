"""yiss.iosxr.mpls"""
import json

import xmltodict

from yiss.decorators import require_model


class MPLS:
    @require_model
    def show_l2vpn_xconnect(
        self, full_output: bool = False, to_json: bool = False,
    ):
        """
        Gather output for 'show l2vpn xconnect' via netconf

        Args:
            full_output: return full xml output from netconf request before parsing
            to_json: return json output instead of dict

        Returns:
            resp: response as xml|json|dict

        RP/0/RP0/CPU0:abc1.sea99#show l2vpn xconnect
        Tue Dec 24 19:52:19.081 UTC
        Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
                SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

        XConnect                   Segment 1                       Segment 2
        Group      Name       ST   Description            ST       Description            ST
        ------------------------   -----------------------------   -----------------------------
        TYPE4      CM-CM-SEA-SEA-00100
                              DN   Hu0/0/1/0.100          UP       172.16.32.3    100    DN
        ----------------------------------------------------------------------------------------
        """
        resp = self.get(self.get_filter())

        if full_output:
            return resp
        resp = xmltodict.parse(resp.xml)
        resp = resp["rpc-reply"]["data"]["l2vpnv2"]["active"]["xconnects"]["xconnect"]

        if to_json:
            return json.dumps(resp)
        return resp

    @require_model
    def show_mpls_traffic_eng_tunnels_brief(
        self, full_output: bool = False, to_json: bool = False,
    ):
        """
        Gather output for 'show mpls traffic-eng tunnels_brief' via netconf

        Args:
            full_output: return full xml output from netconf request before parsing
            to_json: return json output instead of dict

        Returns:
            resp: response as xml|json|dict

        RP/0/RP0/CPU0:abc1.sea99#show mpls traffic-eng tunnels brief
        Mon Dec 23 23:21:22.174 UTC

                             TUNNEL NAME         DESTINATION      STATUS  STATE
                      Bypass->10.10.10.0      172.16.32.1            up  up
                      Bypass->10.10.10.1      172.16.32.2            up  up
        Displayed 0 (of 0) heads, 2 (of 2) midpoints, 0 (of 0) tails
        Displayed 0 up, 0 down, 0 recovering, 0 recovered heads
        """
        resp = self.get(self.get_filter())

        if full_output:
            return resp
        resp = xmltodict.parse(resp.xml)
        resp = resp["rpc-reply"]["data"]

        if to_json:
            return json.dumps(resp)
        return resp
