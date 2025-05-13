from scapy.all import sniff, IP, TCP, UDP, DNS, DNSQR, Raw, ICMP
import threading
import json
from datetime import time
import time



sniffing = False
packet_buffer = []
max_buffer_size = 10
log_file = "logs/packet_log.json"


def deteckt_packet_type(packet): # Funkcja służy do wyciągania z pakietów informacji o protokole
    if packet.haslayer(DNS): # "packet" to obiekt pochodzący z bilbioteki scapy i reprezentuje pakiet
        return "DNS" # a funkcja .haslayer("xxx") sprawdza czy protokół "xxx"  jest w pakiecie co mowi nam o warstwie danego protokołu (np UDP TCP - warstwa transportowa)
    elif packet.haslayer(ICMP): # warstwa 
        return "ICMP"
    elif packet.haslayer(TCP):
        payload = bytes(packet[TCP].payload) # Jeżeli w pakiecie jest protokół TCP to bierzemy jego payload funkcją .payload i go przeszukujemy 
        if b"HTTP" in payload or b"Host:" in payload: # b"xxx" to ciąg bajtów (a nie zwykły tekst). Szukamy po bajtach czy:
            # b"HTTP" – typowe dla odpowiedzi HTTP
            # b"Host:" – występuje w nagłówkach HTTP (w żądaniu GET)
            # Jeśli znajdziemy HTTP, to mówimy: to HTTP, nie zwykły TCP
            return "HTTP"
        return "TCP" # Jeśli nie ma HTTP, ale jest TCP – zwracamy "TCP"
    elif packet.haslayer("UDP"):
        return "UDP"
    return "OTHER"


def packet_callabck(packet): # Za każdym razem gdy scappy.sniff() przechwyci pakiet to automatycznie wywołuje sie ta funkcja
    global packet_buffer # Zmienna globalna przechowująca ostatnie pakiety

    pkt_type = deteckt_packet_type(packet) # pod tą zmienną jest string np. "ICMP" , "TCP", "OTHER" - wczesniej omówiona funkcja 
    pkt_summary = { #  Tworzymy słownik pkt_summary — czyli streszczenie pakietu
        "timestamp" : time.strftime("%Y-%m-%d %H:%M:%S"), # time.strftime to aktualny czas i godzina
        "src" : packet[IP].src if IP in packet else "N/A", # src źródłowy
        "dst" : packet[IP].dst if IP in packet else "N/A", # dst to adres docelowy
        "proto" : pkt_type, # protokół
        "length" : len(packet) # długosc
    }


    # Bufor pakietow dla GUI
    packet_buffer.append(pkt_summary)
    if len(packet_buffer) > max_buffer_size:
        packet_buffer.pop(0)
    # Jeśli bufor jest za duży (np. >10 wpisów), to usuwamy najstarszy pakiet (pop(0)) — z przodu bufora
    # Czyli bufor trzyma tylko ostatnie pakiety


    # Zapis do logu JSON
    with open(log_file, "a") as f: # Otwieramy plik log_file i dopisujemy na końcu ("a" czyli append)
        f.write(json.dumps(pkt_summary) + "\n") # Zamieniamy słownik pkt_summary na JSON (tekst), dopisujemy go do pliku jako osobną linię


def sniff_packets(): # Główna funkcja sniffująca pakiety
    global sniffing # Globalna zmienna 
    sniffing = True # Flaga 
    sniff(  
        prn=packet_callabck, # dla każdego pakietu wywoła funkcję packet_callabck(packet)
        store = False, # store=False: nie przechowuj pakietów wewnętrznie (oszczędza RAM)
        stop_filter = lambda x : not sniffing # sniffer zatrzyma się kiedy sniffing == False  
        )

def start_sniffing(): # Uruchamia sniffowanie w osobnym wątku (żeby nie blokować głównego programu / GUI)
    t = threading.Thread(
                        target=sniff_packets, # Tworzy nowy wątek (Thread) z funkcją sniff_packets() jako cel
                         daemon=True # daemon=True: wątek automatycznie się kończy, gdy zamkniemy aplikację
                         )
    t.start()


def stop_sniffing():
    global sniffing
    sniffing = False # Flaga

def get_recent_packets(): # Zwraca listę ostatnich pakietów (dla przeglądarki / GUI)
    return list(packet_buffer) # packet_buffer to globalna lista z podsumowaniami pakietów