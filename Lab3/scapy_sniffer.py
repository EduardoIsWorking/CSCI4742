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
    """
    Callback function called for each captured packet.
    Extracts and displays TCP packet information including IP and MAC addresses.
    """
    # Check if packet contains both TCP and IP layers
    if TCP in packet and IP in packet:
        # Extract IP source and destination addresses
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        # Extract TCP source and destination ports
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

        # If packet also contains Ethernet layer (MAC addresses), display them
        if Ether in packet:
            mac_src = packet[Ether].src
            mac_dst = packet[Ether].dst
            print(f"MAC: {mac_src} -> {mac_dst}, IP: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")
        else:
            # Display only IP and port information if Ethernet layer not present
            print(f"IP: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

def start_sniffing():
    """
    Start packet sniffing on eth0 interface.
    Captures only TCP packets (filter="tcp").
    store=0 prevents storing packets in memory to save resources.
    """
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
    """Extract and return source/destination MAC addresses from Ethernet layer."""
    return {
        'Source MAC': packet[Ether].src,
        'Destination MAC': packet[Ether].dst,
    }

def parse_ip(packet):
    """Extract and return IP source/destination addresses and protocol type."""
    return {
        'Source IP': packet[IP].src,
        'Destination IP': packet[IP].dst,
        'Protocol': packet[IP].proto  # Protocol number (6=TCP, 17=UDP, etc.)
    }

def packet_callback(packet):
    """Process captured packets and display both Ethernet and IP layer information."""
    # Only process packets that have both IP and Ethernet layers
    if IP in packet and Ether in packet:
        eth_info = parse_ethernet(packet)
        ip_info = parse_ip(packet)

        print(f"Ethernet: {eth_info}")
        print(f"IP: {ip_info}")

def start_sniffing():
    """Start sniffing on eth0, capturing all IP packets."""
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
    """Extract TCP flags from packet and return as a dictionary of boolean values."""
    flags = packet[TCP].flags
    return {
        'SYN': flags & 0x02 != 0,  # SYN flag (0x02 = 0000 0010)
        'ACK': flags & 0x10 != 0,  # ACK flag (0x10 = 0001 0000)
        'FIN': flags & 0x01 != 0,  # FIN flag (0x01 = 0000 0001)
        'RST': flags & 0x04 != 0   # RST flag (0x04 = 0000 0100)
    }

def parse_tcp(packet):
    """Extract source/destination ports and TCP flags from packet."""
    return {
        'Source Port': packet[TCP].sport,
        'Destination Port': packet[TCP].dport,
        'Flags': parse_tcp_flags(packet)
    }

# 2. Extract UDP Details
def parse_udp(packet):
    """Extract source/destination ports and payload length from UDP packet."""
    return {
        'Source Port': packet[UDP].sport,
        'Destination Port': packet[UDP].dport,
        'Length': packet[UDP].len  # Total UDP length including header
    }

# 3. Update Packet Callback
def packet_callback(packet):
    """Process packets and display either TCP or UDP information."""
    # Display TCP information if packet contains TCP
    if TCP in packet:
        tcp_info = parse_tcp(packet)
        print(f"TCP Info: {tcp_info}")
    # Display UDP information if packet contains UDP
    elif UDP in packet:
        udp_info = parse_udp(packet)
        print(f"UDP Info: {udp_info}")

def start_sniffing():
    """Start sniffing on eth0, capturing TCP or UDP packets."""
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
    """Extract ICMP type, code, and checksum from packet."""
    return {
        'Type': packet[ICMP].type,      # ICMP message type (8=Echo Request, 0=Echo Reply, etc.)
        'Code': packet[ICMP].code,      # ICMP code (provides additional info for the type)
        'Checksum': packet[ICMP].chksum # ICMP checksum for error detection
    }

def packet_callback(packet):
    """Process and display ICMP packet information."""
    if ICMP in packet:
        icmp_info = parse_icmp(packet)
        print(f"ICMP Info: {icmp_info}")

def start_sniffing():
    """Start sniffing on eth0, capturing only ICMP packets."""
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
    """
    Extract and decode HTTP payload from packet.
    Returns the HTTP data if present, otherwise returns None.
    """
    try:
        # Check if packet contains Raw (application layer) payload
        if Raw not in packet:
            return None

        # Decode the raw payload as UTF-8 (ignore decode errors with 'ignore')
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        # Return payload only if it contains "HTTP" (indicating HTTP protocol)
        return payload if "HTTP" in payload else None
    except Exception:
        # Return None if any error occurs during payload extraction/decoding
        return None

def packet_callback(packet):
    """Process packets and display HTTP data on port 80."""
    # Check if packet is TCP and uses port 80 (HTTP)
    if TCP in packet and (packet[TCP].sport == 80 or packet[TCP].dport == 80):
        http_data = parse_http(packet)
        if http_data:
            # Print first 200 characters of HTTP data to keep output readable
            print(f"HTTP Data: {http_data[:200]}")
            print("-" * 60)

def start_sniffing():
    """Start sniffing on eth0, capturing HTTP packets (port 80)."""
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
    """
    Extract and return DNS header fields from a captured packet.
    Only runs when the packet contains a DNS layer.
    """
    if DNS in packet:
        return {
            'Transaction ID': packet[DNS].id,       # DNS transaction identifier used to match queries and responses
            'Questions': packet[DNS].qdcount,       # Number of questions in the DNS Question section
            'Answer RRs': packet[DNS].ancount,      # Number of resource records in the Answer section
            'Authority RRs': packet[DNS].nscount,   # Number of resource records in the Authority section
            'Additional RRs': packet[DNS].arcount   # Number of resource records in the Additional section
        }

def packet_callback(packet):
    """
    Callback function executed for each captured packet.
    Filters to DNS packets and prints parsed DNS header information.
    """
    if DNS in packet:
        dns_info = parse_dns(packet)
        print(f"DNS Info: {dns_info}")

def start_sniffing():
    """
    Start sniffing on eth1 for DNS traffic.
    Captures DNS over UDP (common) and TCP (zone transfers/large responses).
    """
    print("Starting packet sniffing with Scapy (DNS)...")
    sniff(iface="eth1", prn=packet_callback, filter="udp port 53 or tcp port 53", store=0)

if __name__ == "__main__":
    start_sniffing()

# 2. Generate Test Traffic

# 3. Validate the Output
