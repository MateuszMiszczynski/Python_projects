from scapy.all import sniff
import json
from datetime import datetime

def save_packet(packet):
    log_entry = {
        "timestamp" : str(datetime.now()),
        "packet_summary" : str(packet.summary()),
        "raw_data" : str(packet)
    }

