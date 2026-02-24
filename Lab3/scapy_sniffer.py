#
# # Part 2

# ## Task 1: Capturing Packets with Scapy
# 
# pip3 install scapy

#
# 1. Create the Project

# 2. Implement Basic Sniffing
from scapy.all import sniff, Ether, IP, TCP, UDP

def packet_callback(packet):
    if TCP in packet and IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

        if Ether in packet:
            mac_src = packet[Ether].src
            mac_dst = packet[Ether].dst
            print(f"MAC: {mac_src} -> {mac_dst}, IP: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")
        else:
            print(f"IP: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

def start_sniffing():
    print("Starting packet sniffing with Scapy...")
    sniff(iface="eth0", prn=packet_callback, filter="tcp", store=0)

if __name__ == "__main__":
    start_sniffing()

# 3. Generate Test Traffic

# 4. Validate the Output

#
# ## Task 2: Parsing Ethernet and IP Layers

#
# 1. Enchance Packet Parsing
from scapy.all import sniff, Ether, IP

def parse_ethernet(packet):
    return {
        'Source MAC': packet[Ether].src,
        'Destination MAC': packet[Ether].dst,
    }

def parse_ip(packet):
    return {
        'Source IP': packet[IP].src,
        'Destination IP': packet[IP].dst,
        'Protocol': packet[IP].proto
    }

def packet_callback(packet):
    if IP in packet and Ether in packet:
        eth_info = parse_ethernet(packet)
        ip_info = parse_ip(packet)

        print(f"Ethernet: {eth_info}")
        print(f"IP: {ip_info}")

def start_sniffing():
    print("Starting packet sniffing with Scapy (Ethernet + IP)...")
    sniff(iface="eth0", prn=packet_callback, filter="ip", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output

#
# ## Task 3: Parsing Transport Layer (TCP and UDP)

#
# 1. Extract TCP Flags
from scapy.all import sniff, TCP, UDP

def parse_tcp_flags(packet):
    flags = packet[TCP].flags
    return {
        'SYN': flags & 0x02 != 0,
        'ACK': flags & 0x10 != 0,
        'FIN': flags & 0x01 != 0,
        'RST': flags & 0x04 != 0
    }

def parse_tcp(packet):
    return {
        'Source Port': packet[TCP].sport,
        'Destination Port': packet[TCP].dport,
        'Flags': parse_tcp_flags(packet)
    }

# 2. Extract UDP Details
def parse_udp(packet):
    return {
        'Source Port': packet[UDP].sport,
        'Destination Port': packet[UDP].dport,
        'Length': packet[UDP].len
    }

# 3. Update Packet Callback
def packet_callback(packet):
    if TCP in packet:
        tcp_info = parse_tcp(packet)
        print(f"TCP Info: {tcp_info}")
    elif UDP in packet:
        udp_info = parse_udp(packet)
        print(f"UDP Info: {udp_info}")

def start_sniffing():
    print("Starting packet sniffing with Scapy (TCP or UDP)...")
    sniff(iface="eth0", prn=packet_callback, filter="tcp or udp", store=0)

if __name__ == "__main__":
    start_sniffing()

# 4. Generate Test Traffic

# 5. Run the Sniffer

# 6. Run the Sniffer

#
# ## Task 4: Dissecting ICMP Packets

#
# 1. Add ICMP Parsing Function:
from scapy.all import sniff
from scapy.layers.inet import ICMP

def parse_icmp(packet):
    return {
        'Type': packet[ICMP].type,
        'Code': packet[ICMP].code,
        'Checksum': packet[ICMP].chksum
    }

def packet_callback(packet):
    if ICMP in packet:
        icmp_info = parse_icmp(packet)
        print(f"ICMP Info: {icmp_info}")

def start_sniffing():
    print("Starting packet sniffing with Scapy (ICMP)...")
    sniff(iface="eth0", prn=packet_callback, filter="icmp", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output

#
# ## Task 5: Parsing HTTP Packets

#
# 1. Capture HTTP Payload
from scapy.all import sniff, TCP, Raw

def parse_http(packet):
    try:
        # Only attempt decode if there is application payload
        if Raw not in packet:
            return None

        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        return payload if "HTTP" in payload else None
    except Exception:
        return None

def packet_callback(packet):
    if TCP in packet and (packet[TCP].sport == 80 or packet[TCP].dport == 80):
        http_data = parse_http(packet)
        if http_data:
            print(f"HTTP Data: {http_data[:200]}")
            print("-" * 60)

def start_sniffing():
    print("Starting packet sniffing with Scapy (HTTP/80)...")
    sniff(iface="eth0", prn=packet_callback, filter="tcp port 80", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output

#
# ## Task 6: Parsing DNS Packets

#
# 1. Capture DNS Packets
from scapy.all import sniff
from scapy.layers.dns import DNS

def parse_dns(packet):
    if DNS in packet:
        return {
            'Transaction ID': packet[DNS].id,
            'Questions': packet[DNS].qdcount,
            'Answer RRs': packet[DNS].ancount,
            'Authority RRs': packet[DNS].nscount,
            'Additional RRs': packet[DNS].arcount
        }

def packet_callback(packet):
    if DNS in packet:
        dns_info = parse_dns(packet)
        print(f"DNS Info: {dns_info}")

def start_sniffing():
    print("Starting packet sniffing with Scapy (DNS)...")
    sniff(iface="eth1", prn=packet_callback, filter="udp port 53 or tcp port 53", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output
