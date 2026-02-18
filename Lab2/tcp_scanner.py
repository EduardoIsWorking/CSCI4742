import socket
import sys

def tcp_scanner(target, port):
   """
   # 1. Add your comment here (e.g., Why do we use `socket.AF_INET` and `socket.SOCK_STREAM`?)
   socket.AF_INET means that we are using IPv4 addresses which is why it is chosen
   socket.SOCK_STREAM creates a reliable TCP protocol which is used for scanning TCP ports
   together we are able to create an IPv4 TCP socket.
   """
   try:
         tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         """
         # 2. What does settimeout(1) do for the TCP socket?
         we need a check against a filtered port or it could block indefinitely
         a 1sec timeout prevents our script from hanging on non-responsive ports
         """

         tcp_sock.settimeout(1)
         tcp_sock.connect((target, port))
         tcp_sock.close()
         return True
   except:
         """
         # 3. Add your comment here (e.g., What types of exceptions might occur?)
         we have an exceptions to catch everything that is not an open port
         this could be closed ports, filtered ports, timeout errors, bad addresses, etc.
         """

         """
         # 4. Why is it important to handle exceptions in network programming?
         exception handling is important in any programming but especially so in network programming
         as networks can be unstable and unreliable so we need to be able to handle any exceptions
         so that our script does not stall on the first thing that goes wrong
         we want it to continue and skip an issues possible.
         """
         return False

def main():
   """
   # 5. Add your comment here (e.g., Why check for command-line arguments with `len(sys.argv)`?)
   it makes sure that the script is only ran if both the script name and the target IP are provided as arguments
   the script is written to only fuction if 2 arguments are provided
   """

   """
   # 6. What happens if no arguments are passed to the script?
   if would then print the usage of the tcp_scanner.py on the IP and exit, this form of error handling
   is preferred as it allows us to easily see what failed and where
   """
   if len(sys.argv) != 2:
         print("Usage: python tcp_scanner.py <Metasploitable-2_IP>")
         sys.exit(1)

   target = sys.argv[1]
   print(f"Scanning TCP ports on {target}...")
   """
   # 7. Add your comment here (e.g., Why loop through the port range 1-1024?)
   common well-known ports are 0-1023, 1-1024 is specified since 0 is reserved on non functional
   up to 1024 is used since python range is exclusive of the end value and we want to end on 1023
   """
   for port in range(1, 1024):
         if tcp_scanner(target, port):
            print(f"[*] Port {port}/tcp is open")

if __name__ == "__main__":
   main()

   """
   # 8. Does running this script require sudo? Why or why not?

   i do not believe this script would require sudo as we are using TCP connect through a socket
   so this should not require special admin privileges to run, it is just a scanning script
   """