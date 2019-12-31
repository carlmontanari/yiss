"""yiss.iosxr.intf"""
import json

import xmltodict

from yiss.decorators import require_model


class INTF:
    @require_model
    def show_interface(
        self, full_output: bool = False, to_json: bool = False,
    ):
        """
        Gather output for 'show interface' via netconf

        Args:
            full_output: return full xml output from netconf request before parsing
            to_json: return json output instead of dict

        Returns:
            resp: response as xml|json|dict

        RP/0/RP0/CPU0:abc1.sea99#show interface
        Tue Dec 24 13:22:12.310 UTC
        Bundle-Ether1 is up, line protocol is up
          Interface state transitions: 13
          Hardware is Aggregated Ethernet interface(s), address is ffff.ffff.ffff
          Description: "abc1.sea99-abc2.sea99"
          Internet address is 10.10.10.1/31
          MTU 9216 bytes, BW 100000000 Kbit (Max: 100000000 Kbit)
             reliability 255/255, txload 0/255, rxload 0/255
          Encapsulation ARPA,
          Full-duplex, 100000Mb/s
          loopback not set,
          Last link flapped 6w3d
          ARP type ARPA, ARP timeout 04:00:00
            No. of members in this bundle: 1
              HundredGigE0/0/1/5           Full-duplex  100000Mb/s   Active
          Last input 00:00:00, output 00:00:00
          Last clearing of "show interface" counters never
          30 second input rate 8000 bits/sec, 2 packets/sec
          30 second output rate 8000 bits/sec, 2 packets/sec
             42428706 packets input, 13317152087 bytes, 0 total input drops
             0 drops for unrecognized upper-level protocol
             Received 12 broadcast packets, 2446988 multicast packets
                      0 runts, 0 giants, 0 throttles, 0 parity
             0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
             120672418 packets output, 23590800650 bytes, 0 total output drops
             Output 11 broadcast packets, 2434208 multicast packets
             0 output errors, 0 underruns, 0 applique, 0 resets
             0 output buffer failures, 0 output buffers swapped out
             0 carrier transitions
        """
        resp = self.get(self._get_filter())
        if full_output:
            return resp
        resp = xmltodict.parse(resp.xml)
        resp = resp["rpc-reply"]["data"]["interfaces"]["interface"]
        if to_json:
            return json.dumps(resp)
        return resp
