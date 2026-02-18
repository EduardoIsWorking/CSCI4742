import socket
import sys

def udp_dns_scanner(target, port=53):
   """
   # Add your comment here (e.g., Why use `socket.SOCK_DGRAM` for UDP scanning?)
   """
   try:
         udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         udp_sock.settimeout(2.0)  # Add your comment here (e.g., What does `settimeout` do?)

         query = b'\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' \
               b'\x07example\x03com\x00\x00\x01\x00\x01'
         # Add your comment here (e.g., What is the purpose of the `query` variable?)

         udp_sock.sendto(query, (target, port))

         response, _ = udp_sock.recvfrom(512)
         # Add your comment here (e.g., Why use `recvfrom(512)`? What does 512 represent?)

         if response:
            print(f"[*] Port {port}/udp (DNS) is open and responding")
            return True
   except socket.timeout:
         # Add your comment here (e.g., Why is a timeout exception likely in UDP scanning?)
         print(f"[-] Port {port}/udp (DNS) did not respond")
         return False
   finally:
         # Add your comment here (e.g., Why close the socket in the `finally` block?)
         udp_sock.close()

def main():
   """
   # Add your comment here (e.g., What is the purpose of `sys.argv`?)
   """
   if len(sys.argv) != 2:
         print("Usage: python udp_dns_scanner.py <Metasploitable-2_IP>")
         sys.exit(1)

   target = sys.argv[1]
   print(f"Scanning UDP DNS port on {target}...")
   udp_dns_scanner(target)

if __name__ == "__main__":
   main()