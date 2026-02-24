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
    if TCP in packet and IP in packet and Ether in packet:
        # Extract MAC, IP, and port details
        mac_src = packet[Ether].src
        mac_dst = packet[Ether].dst
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

        # Print packet details
        print(f"MAC: {mac_src} -> {mac_dst}, IP: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

def start_sniffing():
    print("Starting packet sniffing with Scapy...")
    sniff(prn=packet_callback, filter="tcp", store=0)

if __name__ == "__main__":
    start_sniffing()

# 3. Generate Test Traffic

# 4. Validate the Output

# Screenshots of of the output showing:
# Captured TCP packets.
# MAC, IP, and TCP port details.

#
# ## Task 2: Parsing Ethernet and IP Layers

#
# 1. Enchance Packet Parsing
from scapy.all import sniff, Ether

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
    # "ip" filter keeps output focused on IP packets
    sniff(prn=packet_callback, filter="ip", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output

# Screenshot of output showing parsed Ethernet and IP layer details.
# Answer these questions:
# How does Scapy simplify the extraction of Ethernet and IP layer fields?
# What is the packet[IP].proto field, and how does it relate to TCP/UDP?

#
# ## Task 3: Parsing Transport Layer (TCP and UDP)

#
# 1. Extract TCP Flags
from scapy.all import TCP, UDP

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
    # Capture both transport protocols for this task
    sniff(prn=packet_callback, filter="tcp or udp", store=0)

if __name__ == "__main__":
    start_sniffing()

# 4. Generate Test Traffic

# 5. Run the Sniffer

# 6. Run the Sniffer

# Screenshot of the output showing TCP and UDP details, including TCP flags and UDP length.
# Answer these questions:
# How do TCP flags help in identifying packet behavior?
# Why is the length field in UDP important, and how does it differ from TCP's behavior?
# What are the primary differences between TCP and UDP in terms of reliability and usage?
# Explain the logic behind a syntax like 'ACK': flags & 0x10 != 0, for identifying whether a flag (e.g. ACK here) is set or not.

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
    print("Starting packet sniffing with Scapy (TCP or UDP)...")
    # Capture both transport protocols for this task
    sniff(iface="eth0", prn=packet_callback, filter="tcp or udp", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output

# Screenshot of the output showing parsed ICMP packets.
# Answer these questions:
# What is the purpose of ICMP packets in networking?
# How are ICMP type and code fields used to differentiate packet types?
# What role does the checksum play in ICMP packets?

#
# ## Task 5: Parsing HTTP Packets

#
# 1. Capture HTTP Payload
def parse_http(packet):
    try:
        payload = bytes(packet[TCP].payload).decode('utf-8')
        return payload if "HTTP" in payload else None
    except UnicodeDecodeError:
        return None

def packet_callback(packet):
    if TCP in packet and (packet[TCP].sport == 80 or packet[TCP].dport == 80):
        http_data = parse_http(packet)
        if http_data:
            print(f"HTTP Data: {http_data[:100]}")

# 2. Generate Test Traffic

# 3. Validate the Output

# Screenshot of output showing HTTP payload data for packets on port 80.
# Answer these questions:
# Why does HTTP operate on port 80 by default?
# What common HTTP methods (e.g., GET, POST) could you identify in the parsed payload?
# What challenges might arise when decoding HTTP data in raw packet captures?

#
# ## Task 6: Parsing DNS Packets

#
# 1. Capture DNS Packets
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

# 2. Generate Test Traffic

# 3. Validate the Output

# Screenshot of output showing DNS transaction ID, question count, and resource records.
# Answer these questions:
# What is the significance of the transaction ID in DNS packets?
# How do the flags in a DNS packet indicate the type of query (e.g., standard query, response)?
# Why does DNS primarily use UDP instead of TCP, and under what circumstances might it use TCP?


