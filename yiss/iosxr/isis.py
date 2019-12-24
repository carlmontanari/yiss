"""yiss.iosxr.isis"""
import json

import xmltodict

from yiss.decorators import require_model


class ISIS:
    @require_model
    def show_isis_adjacency(self, full_output: bool = False, to_json: bool = False):
        """
        Gather output for 'show isis adjacency' via netconf

        Args:
            full_output: return full un-parsed xml output
            to_json: return json output

        Returns:
            resp: response as xml|json|dict

        RP/0/RP0/CPU0:abc1.sea99#show isis adjacency
        Tue Dec 24 13:24:34.423 UTC

        IS-IS cm Level-2 adjacencies:
        System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                                       BFD  BFD
        abc2.sea99     BE1                      *PtoP*         Up    28   9w9d     Yes Up   None
        abc3.sea99     BE2                      *PtoP*         Up    9    9w9d     Yes Up   None

        Total adjacency count: 2
        """
        resp = self.get(self._get_filter())

        if full_output:
            return resp

        resp = xmltodict.parse(resp.xml)
        resp = resp["rpc-reply"]["data"]["isis"]["instances"]["instance"]

        if to_json:
            return json.dumps(resp)
        return resp
