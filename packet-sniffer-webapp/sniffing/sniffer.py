from scapy.all import sniff
import json
from datetime import datetime

def save_packet(packet):
    log_entry = {
        "timestamp" : str(datetime.now()),
        "packet_summary" : str(packet.summary()),
        "raw_data" : str(packet)
    }

    log_filename = f"logs/log_{datatime.now().strftime('%Y-%m-%d')}.json"

    with open(log_filename, "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")


# Funkcja do sniffowania pakietow
def start_sniffing():
    sniff(prn = save_packet, count = 10) # To znaczy żeby zbierał 10 pakietów, można modyfikować

