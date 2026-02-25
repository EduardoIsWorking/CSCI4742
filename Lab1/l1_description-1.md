## **Lab 1: CTI with MITRE ATT&CK, and Bash Scripting**

##### CSCI 5742/CSCY 4742: Cybersecurity Programming and Analytics, Spring 2026
##### Total Points: 100

#### Dustin Nguyen, Blanca Duizar Huenas, Eduardo Galvez
---

### **Introduction**
This lab is designed to provide students with a comprehensive, hands-on experience in cybersecurity. It is divided into three interconnected parts:

1. **Bash Scripting for Cybersecurity**: Learn and apply Bash scripting skills to automate essential cybersecurity operations, such as system monitoring, log analysis, and detecting suspicious activity.
   
2. **CTI Training with MITRE ATT&CK**: Explore Cyber Threat Intelligence (CTI) through the MITRE ATT&CK framework. Analyze an Advanced Persistent Threat (APT) campaign, map adversarial behaviors to tactics and techniques, and gain insights into adversarial actions.

---

### **Lab Structure and Point Breakdown**

| **Part**                          | **Description**                                                   | **Points** |
|-----------------------------------|-------------------------------------------------------------------|------------|
| **Part 1: Linux Basics and Bash**        | Writing and executing Bash scripts to automate cybersecurity tasks, with extensions. | 20         |
| **Part 2: CTI with MITRE ATT&CK** | Mapping adversarial behaviors from a narrative report to MITRE ATT&CK tactics and techniques. | 55         |
| **Total**                         |                                                                   | **100**    |

---
### **Part 1: Bash Scripting for Cybersecurity**

#### **Objective**
This section introduces **Bash scripting** with a focus on cybersecurity tasks. The goal is to learn basic scripting concepts in Linux.



---
### *Tasks for Part 1*

#### **Preparation - Step 1: Prepare Your Virtual Machines**

1. **If you haven't already, follow the [Testbed Setup Guideline](../testbed_setup/testbed_setup_main.html) to configure your lab environment**.
2. **Power On the Kali VMs and Metasploitable-2 Target VM**.

3. **Log Into VMs and MS-2 and Verify Their Connectivity via Pings**.

4. **Verify Internet Connectivity (Optional)**:
   - If **Adapter 2** is configured as **NAT** for Internet access on Kali VMs, confirm connectivity by running the following command:
     ```bash
     ping -c 4 google.com
     ```
   - If the `ping` command is unsuccessful and you see `Destination Host Unreachable` or similar messages, it may indicate that ICMP traffic is blocked by the host or network in NAT mode. In this case, use the following command to verify Internet access via HTTP/HTTPS:
     ```bash
     curl -I https://www.google.com
     ```
   - If `curl` returns HTTP response headers (e.g., `HTTP/1.1 200 OK`), Internet access is functioning, and the issue is limited to ICMP traffic being blocked.

---

#### **Preparation - Step 2: Familiarize Yourself with Linux Bash Commands**

##### Introduction to Bash (Bourne Again Shell)

- Bash is a command-line interpreter (shell) used in Unix-based operating systems (Linux, macOS).
- It allows users to interact with the OS by executing commands directly.
- You can run commands interactively in a terminal.

   ```bash
   ls -l
   echo "Hello, World!"
   ```
- In this case, you type commands one by one, and they execute immediately.

##### **Bash Scripting**
- Bash scripting refers to writing a series of commands in a file (script) to be executed sequentially.
- It allows automation, conditional execution, loops, and function definitions.
- A Bash script typically starts with `#!/bin/bash` (shebang) and is saved with a `.sh` extension.

- **Example: A simple Bash script (`myscript.sh`)**
   ```bash
   #!/bin/bash
   echo "Hello, World!"
   ls -l
   ```

- To execute the script:
   ```bash
   chmod +x myscript.sh  # Make the script executable
   ./myscript.sh         # Run the script
   ```

- In short, **Bash** is the shell you use, while **Bash scripting** is a way to automate tasks by writing scripts.

##### **Tasks for Self-Practice**
Run these commands in Kali VMs and Metasploitable-2 VM and inspect the results carefully, aiming for understanding the purpose and cybsersecurity uses of each command:

1. **System Information Commands**:
   - Familiarize yourself with commands to gather system information:
     ```bash
     uname -a        # Display system and kernel information
     whoami          # Display current user
     id              # Display user and group IDs
     ```

2. **Networking Commands**:
   - Explore basic networking utilities:
     ```bash
      ip addr show            # Display network interfaces and IP addresses
      ping -c 4 <IP Address>  # Test connectivity to a target
      arp -a                  # Display the ARP table
      netstat -tuln           # Show open TCP/UDP ports
      nmap -sP 192.168.x.0/24 # Ping scan to identify active hosts in the specified subnet
      route -n                # Display the routing table
      ss -tuln                # Show active connections and listening ports
      nc <IP Address> <Port> # Test TCP connection to a specific port
     ```

   3. **Interacting with HTTP on Metasploitable-2 (Target VM) via Netcat**

   Use `nc` (netcat) to interact with the HTTP service running on Metasploitable-2. Follow these steps:

   1. **Connect to Port 80**:
      ```bash
      nc <Metasploitable-2 IP> 80
      ```

   2. **Send an HTTP GET Request**:
      - After connecting, type the following line and press Enter twice:
      ```
      GET / HTTP/1.1
      Host: <Metasploitable-2 IP>
      ```

   3. **Observe the Response**:
      - Analyze the HTTP response headers and any HTML content returned by the server.

4. **Downloading Files with `curl` and `wget`**
   - These tools are essential for retrieving data from web servers:
     - `curl`: Fetches HTTP headers to verify if a web resource is reachable.
       ```bash
       curl -I http://http.kali.org/kali/dists/kali-rolling/InRelease
       ```  
     - `wget`: Downloads files from web servers.
       ```bash
       wget http://http.kali.org/kali/dists/kali-rolling/InRelease
       ```  

   - **When to Use `sudo` with `curl` or `wget`**:
     - Not needed for downloading files to user-owned directories.
     - Needed if saving files in system-protected locations (e.g., `/etc`, `/usr/local`).

> **Using `sudo` for Networking Commands**: Some commands (e.g., `netstat`, `nmap`, or `arp`) require administrator privileges. This is because they interact with low-level system configurations or monitor network traffic, which are sensitive operations.
>  - `sudo` (short for "superuser do") allows non-administrative users to execute commands with elevated privileges temporarily.  
>  - It ensures security by limiting direct access to the root account.  
>  - **Common Scenarios Requiring `sudo`**:
>    - Scanning networks (`nmap`, `arp`, `tcpdump`).
>    - Editing system configuration files.
>    - Managing packages and updates (`apt update`, `apt install`).
> - For more information about `sudo`, refer to the document [Understanding Sudo and Administrative Privileges in Linux](sudo.md) .

---

#### **Task 1: Writing a Bash Script**
1. **Create a Bash Script**:
   - Open a terminal on the **Kali Attack VM**. You have two options for editing:
     - **GUI Option** (Beginner-Friendly): Use the **Mousepad** text editor, which provides a graphical user interface:
       ```bash
       mousepad basic_security.sh
       ```
     - **Command-Line Option** (Recommended for Professionals): Use **Nano** or **Vi**, widely used by professionals for editing files directly in the terminal:
       ```bash
       nano basic_security.sh
       ```
       or
       ```bash
       vi basic_security.sh
       ```

   - While Mousepad is more beginner-friendly, learning **Nano** or **Vi** is highly recommended for working efficiently on remote servers or systems without a GUI.


2. **Write the Script Code**:
   - Add the following code to your script. Replace **x** with your own subnet (e.g., 192.168.10.0/24) and target (MS-2 Target VM) IP addresses:
     ```bash
      #!/bin/bash
      # Variables
      # CORRECTION 1: previous "SUBNET="192.168.10.101""
      SUBNET="192.168.10.0/24"    # Replace 'x' with the local subnet network address for your environment
      TARGET="192.168.10.101"       # Replace with the target IP or host IP (MS-2 Target VM)

      echo "Enhanced Security Script"
      echo "========================="

      # Part 1: Collect Information About the Local Machine
      echo "Part 1: Information About My Own Machine"
      echo "========================================="
      echo "[*] System Information:"
      uname -a   # This command displays the current system information
      echo

      echo "[*] Network Interfaces and IP Addresses:"
      ip addr show   # This command displays the current network interfaces and IP addresses of the system
      echo

      echo "[*] ARP Table:"
      arp -a   # This displays the Address Resolution Protocol table
      echo

      echo "[*] Open Ports on Local Machine:"
      sudo netstat -tuln   # Shows the current open TCP and UDP ports. It is also listening sockets and numeric addresses (what the ln is for).

      echo

      # Part 2: Collect Information About a Target
      echo "Part 2: Information About a Target"
      echo "=================================="
      echo "[*] Active Hosts in Subnet ($SUBNET):"
      sudo nmap -sP $SUBNET   # This gives a ping scan and identifies active hosts in the subnet.
      echo

      # CORRECTION 2: previous "This command sends ICMP echo requests and TCP ACK pings to see what hosts are available. -sV probes open ports to detect the server."
      echo "[*] Service Scan on Target ($TARGET):"
      sudo nmap -sV $TARGET   # This command specifically scans host target for any open ports to identify services and exact versions. This is crucial during reconnaisance as it allows attacks to know exactly what services they are facing and able to easily check if any of the current versions of the software contain known vulnerabilities.
      echo

      echo "[*] Vulnerability Scan on Target ($TARGET):"
      sudo nmap --script vuln $TARGET   # This will run nmap's vulnerability detection scripts against the target system. --script vuln will load the vuln category and check for known vulnerabilities within the nmap database.
      echo
      ```

     

3. **Save and Exit the File**:  
   - After writing your script, follow these steps based on the text editor used:
     - **Nano**:
       - Press `Ctrl + O` to save the file, then press `Enter` to confirm.
       - Press `Ctrl + X` to exit Nano.
     - **Mousepad** (GUI Editor):
       - Click **File > Save**, then close the editor.
     - **Vim**:
       - Press `Esc`, type `:wq`, and press `Enter` to save and exit.

4. **Make the Script Executable**:
   - In the terminal, navigate to the directory containing your script (use `cd` if needed).
   - Run the following command to make your script executable:
     ```bash
     chmod +x basic_security.sh
     ```

5. **Test the Script**:
   - Run the script to verify it works:
     ```bash
     ./basic_security.sh
     ```
   - If it runs successfully, your script is ready for further development.

6. **Run the Script**:
   - Execute the script:
     ```bash
     ./basic_security.sh
     ```

---

### *Part 1 Deliverables*

**Respond in the [Lab 1 Report File](l1_report.md) with the following deliverables:**

1. **Fully Commented Bash Script**:
   - Submit the **Bash script file** (`basic_security.sh`) with the following:
     - Replace placeholder comments (`# Add comment here`) with your explanations, providing detailed explanation of what each command does.
     - Each comment should explain:
       - The purpose of the section or command.
       - The options or flags used in commands (e.g., `-sP` in `nmap` or `-tuln` in `netstat`).

2. **Screenshots**:
   - Include screenshots showing:
     - The script running successfully in the terminal.
     - ![Working Bash Script.png](Screenshots/Working%20Bash%20Script.png)
     - Output for:
       - Active hosts in the subnet (`nmap -sP`).
       - ![nmap -sP.png](Screenshots/nmap%20-sP.png)
       - Service scan results for the target machine (`nmap -sV`).
       - ![nmap -sV.png](Screenshots/nmap%20-sV.png)
       - Vulnerability scan results for the target machine (`nmap --script vuln`).
       - ![nmap --script vuln.png](Screenshots/nmap%20--script%20vuln.png)
     - Errors, if encountered, along with an explanation of how you resolved them.

3. **Summary and Analysis Report**:
   - Write a **200-500 words** report that includes:
     - **Purpose of the Script**: Describe what the script does and why it is useful for network security tasks.
     - **Challenges Faced**: List any issues encountered during development or execution of the script and how you resolved them.
     - **Extensions Added**: Mention any modifications or additional features you implemented beyond the provided code (e.g., extra scans, error handling, custom variables).
* The primary purpose of this bash script is to first inform the user about their own machine. It first tells them about their current system information- the operating system and the version that it is currently using. After that, it will then tell the user about their current network interfaces and the broadcast address, which will be used to ping other network devices within the network. This also shows the MAC address and the current status of the interface. There are three different interfaces shown, with eth0 being the main ethernet network, and can be used for simultaneous connections or for network segmentation. Afterwards, an ARP table is shown. This lists the devices that the machine has recently communicated with on the local network. Then, a list of current open ports will also be shown, but will need specific admin privileges, which is what the sudo command is used for, which will then listen to TCP/UDP ports and services on the local machine. In this case, no ports are currently open. For part two of the bash script, it shows the the active hosts that are alive through ping sweeps. This is called Active Host Discovery. One IP address is found during this sweep. Then, service enumeration is performed, which identifies open ports and determines their service and version information. Lastly, vulnerability detection is scripted, and it runs the nmap vulnerability scan to detect known vulnerabilities on the system. This bash script is extremely useful for defense, as it will be able to network inventory and assess current vulnerabilities. For attackers, it can be used for reconnaissance to map networks, discover targets and identify vulnerabilities, so it should have specific access to run, most likely root privileges. While running this script, I had no issues trying to get it to run, simply by running ipconfig on the metasploitable machine and plugging it in allowed the program to work flawlessly. I used the command-line option to run everything to make sure I am using industry standard tools as well. 
---

#### **Assessment Rubric for Part 1 (35 Points)**

| **Task**                         | **Criteria**                                                                                           | **Points** |
|----------------------------------|-------------------------------------------------------------------------------------------------------|------------|
| **Bash Script**                  | Script includes all required functionalities (e.g., system information, open ports, failed login checks) and runs without errors. | 10         |
| **Documentation and Comments**   | Script is fully documented with clear, accurate, and meaningful comments explaining the purpose and functionality of each command. | 15          |
| **Report and Screenshots**       | The report is well-organized, concise, and demonstrates a strong understanding of the script's purpose and execution. Required screenshots are included, clear, and relevant. | 10          |

<div style="text-align: center; margin: 15px 1;">
    <hr style="border: 5px; height: 20px; width: 100%;">
</div>


### **Part 2: CTI Training with MITRE ATT&CK**

#### **Objective**
This lab introduces students to Cyber Threat Intelligence (CTI) using the MITRE ATT&CK framework. Students will analyze a narrative threat report on a cutting-edge APT campaign and map adversarial behaviors to tactics, techniques, and sub-techniques using ATT&CK. The goal is to familiarize students with adversarial behaviors, the attack lifecycle, and CTI analysis through hands-on practice.

---

#### **Preparation (Pre-Lab Work)**

#### **Video Training Instructions (MITRE CTI Training - Module 1)**  


##### **Step 1: Explore the MITRE CTI Training Resources**  
- Visit the MITRE ATT&CK® Cyber Threat Intelligence (CTI) training page:  
  [MITRE CTI Training](https://attack.mitre.org/resources/learn-more-about-attack/training/cti/)  
- Familiarize yourself with the training structure and available resources.

##### **Step 2: Watch the Module 1 Training Video**  
- **Video Title:** *Mapping to ATT&CK from Narrative Reporting*  
- **Watch here:** [YouTube - MITRE CTI Training (Module 1)](https://www.youtube.com/watch?v=jRIJ5nw4GMA&list=PLLGRmm150VfBd_bk6fGqTqxr8SBeDcprb&index=2)  
- **Duration:** The first **37 minutes** provide core content, but watching the full video is strongly recommended for a comprehensive understanding.

##### **Step 3: Review the Module 1 Training Slides**  
- Download and review the **official slides** for Module 1:  
  [Module 1 Slides (PDF)](https://attack.mitre.org/docs/training-cti/Module%201%20Slides.pdf)  
- The slides reinforce key concepts covered in the video.

##### **Step 4: Explore ATT&CK Matrix**:
   - Visit the [MITRE ATT&CK Matrix](https://attack.mitre.org/matrices/enterprise/) and review:
     - The 14 tactics (e.g., Initial Access, Discovery, Persistence).
     - Common techniques and sub-techniques under each tactic.


---

### *Tasks for Part 2*

#### **Preparation: Review the Threat Report**

1. **Read the Report**:
   - Carefully review the report: [*Cutting Edge APT Campaign: 2023–2024 Cyber Espionage Targeting ICS Vulnerabilities*](CuttingEdge_APT_report.html).
   - Focus on sections that describe adversarial actions, such as:
     - Exploitation pathways (e.g., CVE-2024-21887).
     - Malware behavior (e.g., ZIPLINE, THINSPOOL).
     - Command-and-Control infrastructure.
     - Adversarial objectives (e.g., intellectual property theft, persistent access).

2. **Highlight Key Behaviors**:
   - Identify descriptions of what the adversary *did*. Look for actionable phrases (e.g., "exploited vulnerabilities," "deployed malware").
   - Example behaviors from the report:
     - **Behavior**: "Exploited CVE-2024-21893 to perform reconnaissance."
     - **Behavior**: "Deployed ZIPLINE backdoor to ensure persistence."

---

#### **Task 1: Map Behaviors to MITRE ATT&CK**

**1. Extract Behaviors**:
   - Read the narrative threat report carefully, focusing on actionable adversarial behaviors (verbs like *scanned*, *exploited*, *deployed*, *gathered*).
   - Write down all the behaviors that describe what the adversary *did*, not just their intentions or outcomes.
   - Example behaviors:
     - "Performed network scans using a custom Python script."
     - "Exploited CVE-2024-21893 to gain initial access."
     - "Deployed malware to establish persistence."


   
**2. Complete this mapping process for *at least 5 unique behaviors* identified in the report, excluding the provided examples below. For each technique:**

   - ##### **Identify the Tactic**
     - **Definition**: A **tactic** represents the adversary's **goal** or **objective** at a specific phase of the attack lifecycle.
     - **Reference the ATT&CK Matrix**:
       - Tactics are the **columns** in the ATT&CK Matrix (e.g., Reconnaissance, Initial Access, Execution).
     - **Ask Yourself**:
       - What is the adversary trying to achieve with this behavior?

   - ##### **Identify the Technique/Sub-Technique**
     - **Definition**: A **technique** is the specific method used by the adversary to achieve the goal (tactic). Sub-techniques are more detailed implementations of a technique.
     - **Steps to Match**:
       1. Go to the [MITRE ATT&CK Matrix](https://attack.mitre.org/matrices/enterprise/).
       2. Look under the identified tactic to find a relevant technique or sub-technique.
       3. Use keywords from the behavior (e.g., "scanning," "vulnerability exploitation") to narrow down possibilities.
     - **Ask Yourself**:
       - What specific method does this behavior describe?

   - ##### **Document Your Findings**
     1. **Behavior Description**:  
        - Write a concise summary of the adversarial behavior from the threat report. Use exact phrasing or paraphrase to capture the essence.

     2. **Tactic**:  
        - Identify the primary objective the adversary was trying to achieve.

     3. **Technique**:  
        - Specify the exact technique used.

     4. **Justification**:  
        - Explain why you chose this tactic and technique.
        - Address:
          - What evidence in the report supports this mapping?
          - How does the behavior align with the selected tactic and technique?


---
#### Example of Mappings

##### **Example 1: Achieving Persistence Through Malware Deployment**
- **Behavior**:  
  Attackers deployed the **ZIPLINE** backdoor, which embedded itself into core system libraries like `libsecure.so`, hijacked incoming traffic, and triggered malicious operations such as reverse shell activation and file transfers.
  
- **Mapping Process**:
  1. **Tactic**: **Persistence**  
     - Objective: Maintain long-term access to the system.
  2. **Technique**: **T1547 - Boot or Logon Autostart Execution**  
     - Sub-Technique: **T1547.001 - Registry Run Keys/Startup Folder**
  3. **Justification**:  
     ZIPLINE altered system startup files to maintain persistence across reboots. The use of core library modification aligns with the Persistence tactic and Boot or Logon Autostart Execution technique, ensuring consistent access to the compromised system.

##### **Example 2: Data Exfiltration via Secure Channels**
- **Behavior**:  
  Attackers fragmented sensitive files, encrypted them using AES-256, Base64-encoded the data, and transmitted it via **TLS 1.3** to a command-and-control server over HTTPS, mimicking legitimate API traffic.
  
- **Mapping Process**:
  1. **Tactic**: **Exfiltration**  
     - Objective: Transfer sensitive data covertly.
  2. **Technique**: **T1041 - Exfiltration Over C2 Channel**
  3. **Justification**:  
     The adversary encrypted and disguised exfiltrated data within legitimate HTTPS traffic to avoid detection, aligning with Exfiltration tactics and Exfiltration Over C2 Channel techniques.

##### **Example 3: Privilege Escalation via Command Injection**
- **Behavior**:  
  Using **CVE-2024-21887**, the attackers exploited input validation flaws in ICS system management scripts, embedding shell commands to gain administrative privileges.
  
- **Mapping Process**:
  1. **Tactic**: **Privilege Escalation**  
     - Objective: Elevate permissions to administrative levels.
  2. **Technique**: **T1059 - Command and Scripting Interpreter**  
     - Sub-Technique: **T1059.004 - Unix Shell**
  3. **Justification**:  
     The behavior leveraged unsanitized input fields to execute arbitrary commands with administrative privileges. This aligns with the Privilege Escalation tactic and Unix Shell technique, as the attackers directly manipulated the command-line interface.

#### **Behavior **
##### **Document Your Findings**

---
[*Cutting Edge APT Campaign: 2023–2024 Cyber Espionage Targeting ICS Vulnerabilities*](CuttingEdge_APT_report.html).
- **Behavior 1:**   
Using **CVE-2023-46805**, the adversary sent malformed HTTP requests and forged authentication tokens to bypass the authentication mechanism on the Ivanti ICS appliance, gaining access while appearing to be a legitimate user. The vulnerabilities were found and exploited, allowing the actor to create malicious requests.
- **Mapping Process**:
- **Tactic: Initial Access**   
Objective:
The adversary gains an unauthorized foothold on an internet-facing host by exploiting a vulnerability to bypass authentication controls.
- **Technique:** **T1190 - Exploit Public-Facing Application**   
  - Sub-Technique: NONE
- **Justification:**
The report found that the combination of malformed HTTP requests and forged authentication tokens was used to make it appear that legitimate users were accessing the system. In ATT&CK, this aligns with T1190, which involves exploiting a weakness in a public-facing application. The authentication was bypassed when custom-encoded HTTP headers were used to bypass security.
---
[*Cutting Edge APT Campaign: 2023–2024 Cyber Espionage Targeting ICS Vulnerabilities – A Technical Summary*](https://olucdenver-my.sharepoint.com/personal/yash_hindocha_ucdenver_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fyash%5Fhindocha%5Fucdenver%5Fedu%2FDocuments%2FCuttingEdge%5FAPT%5Freport%2Ehtml&parent=%2Fpersonal%2Fyash%5Fhindocha%5Fucdenver%5Fedu%2FDocuments&ga=1)

- **Behavior 2**:
Manipulated Unix domain sockets by using PITSTOP, which creates hidden communication between processes on the same machine, in combination with PITHOOK, which creates persistent access by monitoring through hooking key web server functions.
- **Mapping Process**:
  1. **Tactic**:  **Persistence**
   2. Objective: **ID: TA0003** The adversary wants to maintain access and be resident to the system by maintaining a foothold in Ivanti Connect Secure with the goal of long-term access. Hijacking legitimate code gives access.
  3. ~~**Technique**: **T1574 - Hijack Execution Flow**~~ 
   **Technique: T1505 - Server Software Component**
     - Sub-Technique: N/A
  4. **Justification**:
The behavior aligns with the tactic TA0003 because the SparkGateway plugin starts automatically, which makes the attacker's code start, and the adversary stays in the system. The adversary executes their malicious code by hijacking the system since the path is trusted by the user. *By installing the malicious components is allows the adversay to extend and abuse server applications.*
---
[*Cutting Edge APT Campaign: 2023–2024 Cyber Espionage Targeting ICS Vulnerabilities – A Technical Summary*](https://olucdenver-my.sharepoint.com/personal/yash_hindocha_ucdenver_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fyash%5Fhindocha%5Fucdenver%5Fedu%2FDocuments%2FCuttingEdge%5FAPT%5Freport%2Ehtml&parent=%2Fpersonal%2Fyash%5Fhindocha%5Fucdenver%5Fedu%2FDocuments&ga=1)
- **Behavior 3**:
The adversary uses VPN pivoting: it compromises endpoints by using the private client network via the compromised machine, then accesses the remote VPN server to reach deep into the network. It uses encrypted tunnels in cybersecurity to encapsulate malicious traffic. Encapsulation is used to mask the real IP address so it cannot be detected and bypasses network filters.
- **Mapping Process**:
  1. **Tactic**: **Command and Control**
Objective: ID: **TA0011**. The adversary wants to move from the client to the server, or from one endpoint to another, using VPN pivoting, which can give them access to internal resources that are not accessible from the outside.
  1. **Technique**: **T1090** **Proxy**
     - Sub-Technique: Internal Proxy T1090.001
  2. **Justification**: 
The behavior maps to the TA0011 tactic because the attacker can access and communicate with the internal network. The technique allows the adversary to direct internal network traffic between systems and mimic legitimate encrypted communications. By using an internal proxy, the adversary can manage communications inside the compromised environment and avoid suspicion by riding over existing trusted paths
---
[Gaining Credentials Through Embedding ICS Web Interfaces]()
 - **Behavior 4**:
WARPWIRE is a specialized JavaScript-based credential harvester by intercepting and exfiltrating plaintext credentials with Base64-encoded HTTP GET requests enabling lateral movement.
- **Mapping Process**:
  1. **Tactic: Credential Access**
     1. Objective: The adversary is trying to steal account credentials
  2. **Technique**: **T1056 - Input Capture**
     - Sub-Technique: **T1056.003 - Web Portal Capture**
  3. **Justification**:
While initially I thought the tactic from WARPWIRE was Lateral Movement, Credential Access would be the correct tactic. WARPWIRE enabled but did not directly do Lateral Movement. From its actions of intercepting and exfiltration it was able to do Credential Access from captured ICS web interfaces, capturing web portal login credentials input. This was done through a web portal.
---

[Backdoor Persistence through Server Software Modification]()
 - **Behavior 5**:
PITHOOK hooked critical web server functions within ICS appliances to establish and maintain a persistent backdoor.
- **Mapping Process**:
  1. **Tactic**: **Persistence**
   2. Objective:**The adversary is trying to maintain their foothold through consistent backdoor access.**  
  3. **Technique**: **T1505 - Server Software Component**  
     - Sub-Technique: NONE
  4. **Justification**:
The goal of PITHOOK was to maintain a consistent backdoor access using web server functions, BASE64 and AES, that are commonly used for enterprise server applications aligning with T1505. So we know the main tactic is persistence and Server Software Component would be the technique as  the goal is to extend and abuse these enterprise server applications.

---

Summary

 While MITRE ATT&CK is a large community database that includes different techniques, tactics, behaviors and justifications behind the attacks, it also provides relevant attacks based on the technique or behavior. In this instance, the group researched multiple different behaviors, spanning from forged authentication tokens, to manipulating unix domain sockets using PITSTOP and then abused with PITHOOK, to VPN pivotng by compromising endpoints, even intercepting and exfiltrating plaintext credentials with WARPWIRE. MITRE ATT&CK is perfect for mapping the correct tactics and techniques for specific behaviors within dvanced persistent threats. With the first behavior, T1190, it exploited public-facing applications by using malformed HTTP requests, so attackers appeared as legitimate users to ICS facing applications. Attackers in this sense wanted to gain unauthorized control to these applications without triggering alerts. By using malformed HTTP requests, they loooked like legitimate traffic to these ICS networks. For behavior 2, the APT was able to manipulate Unix domain sockets to enable hidden inter-process communication, allowing malicious code to execute within a trusted system without triggering alerts. This seems like a much more complicated version of behavior one, and also includes the behavior of persistance by making sure they maintained long-term access on ICS environments. Behavior 3 used lateral movement along with a compromised Ivanti appliance as a VPN pivot point. This meant that once an attacker was able to gain hold of this device, they were able to encapsulate malicious traffic within the legitimate VPN tunnels of the compromised device and route attacks from the edge device, finding more private ICS networks and "live off the land." Through abusing the existing VPN technology, APTs were able to enforce network segmentation and exfiltrate data through legitimate networks. WARPWIRE was able to harvest credentials through both lateral movement and privilege escalation through ICS networks. Since adversaries hired through nation-state actors will typically use reconnaissance to model the best way to attack a system, they will most likely use lateral movement to find the best method to attack. In this sense, the APT was able to capture plaintext usernames through legitimate ICS web login interfaces through a JavaScript injector, just before they reached an authentication backend. This allowed the adversary to take over accounts without cracking passwords or using brute force. Lastly, the fifth behavior used PITHOOK purely for cyber espionage. This was where the threat did not want to disrupt ICS operations, meaning that they most likely wanted to use tools within native devices, blend in with normal network traffic and possibly exfiltrate information out of the target. The reports were unforunately inconsistent, however it makes sense due to the urgency and accuracy needed for the reports to be sent out to the community efficiently. With so many techniques and mappings, it may be hard for experts to understand the information clearly, but by reading the summaries and getting used to the formatting, it is much easier to understand the reports. Lastly, it is pertinent to map these adversarial behaviors to specific tactics and threats. This allows experts to easily browse the correct formats and find the processes within the techniques and sub-techniques. The process of understanding MITRE ATT&CK is perfect for a beginner trying to learn the different behaviors of adversaries, and would most likely be used within a real-world context during attacks, warning users to keep updated on software versions, network access controls and different types of cyber attacks.
 
 ---
 
### *Part 2 Deliverables*


**Respond in the [Lab 1 Report File](l1_report.md) with the following deliverables:**

**1. Mapping List**: Submit a completed mapping list for *at least 5 unique behaviors* identified from the report. The list must include:
   - **Behavior**: A concise description of the adversarial action.
   - **Tactic**: The primary goal associated with the behavior (e.g., Reconnaissance, Persistence).
   - **Technique/Sub-Technique**: The specific method used, with technique ID (e.g., Active Scanning - T1595).
   - **Justification**: A brief explanation (one or two sentences) of why the chosen tactic and technique were selected. Refer to evidence from the report and explain how it aligns with the ATT&CK framework.

   Ensure all mappings are distinct, well-researched, and aligned with the behaviors described in the report.

**2. Summary and Analysis Report**: Submit a **300–500 word report** summarizing your findings and reflecting on the mapping process. The report must address the following points:

1. **Key Adversarial Behaviors**:
   - Provide a high-level summary of the significant adversarial behaviors observed in the campaign.
   - Highlight how these behaviors demonstrate the attackers’ objectives and technical sophistication.

2. **Challenges in Mapping Behaviors**:
   - Describe the challenges encountered during the mapping process (e.g., ambiguities in the report, unfamiliar techniques).
   - Explain how you resolved these challenges, such as by consulting ATT&CK documentation or training materials.

3. **Insights and Lessons Learned**:
   - Reflect on the value of mapping adversarial behaviors to tactics and techniques.
   - Discuss how this process has enhanced your understanding of CTI and the ATT&CK framework.
   - Mention how this experience is applicable to real-world cybersecurity tasks.



---
#### **Part 2 Assessment Rubric (65 Points)**

| **Task**                 | **Criteria**                                                                 | **Points** |
|--------------------------|------------------------------------------------------------------------------|------------|
| **Mapping List**         | Detailed and accurate mapping of at least 5 unique behaviors to tactics and techniques. Justifications are evidence-based and align with the ATT&CK framework. | 40         |
| **Summary and Analysis Quality**       | Clear, concise summary addressing key adversarial behaviors, challenges, and insights gained from using the MITRE ATT&CK framework. | 15         |
| **Documentation Quality**       | Well-organized and properly formatted documentation, including clear explanations, appropriate use of references, and adherence to the provided report template. | 10         |

<div style="text-align: center; margin: 15px 1;">
    <hr style="border: 5px; height: 20px; width: 100%;">
</div>

### **Lab 1 Submission Guidelines**

1. **Complete Lab 1 Report**:  
   - Download the provided [*lab 1 report file*](l1_report.md).  
   - Complete the report by filling out all required sections.

2. **Bash Script**:  
   - Include your **Bash script file** (`basic_security.sh`) as a standalone file within the submission folder.

3. **Screenshots**:  
   - Ensure all screenshots referenced in the report are included in the submission folder:
     - Place all screenshots in a subfolder named **`screenshots`** within the same directory as your `l1_report.md` file.  
     - To embed a screenshot in the report, use the following Markdown syntax:  
       ```markdown
       ![Screenshot Description](./screenshots/filename.png)
       ```
       Replace `filename.png` with the actual name of the screenshot file, and provide a clear description for accessibility.

4. **Submission Format**:  
   - Combine all files (**`l1_report.md`**, `basic_security.sh`, and the **`screenshots`** folder) into a compressed **`.zip`** file.  
   - Name the compressed file as **`Lab1.zip`**.

5. **PDF Option** (Optional):  
   - If converting the `.md` file to PDF:
     - Ensure all formatting, including headings, code blocks, and screenshots, is preserved.
     - Include the **`basic_security.sh`** file and screenshots folder in the submission, alongside the PDF, within the `.zip` file.

6. **Final Submission**:  
   - Upload the `.zip` file to the course’s Canvas page by the deadline.


<div style="text-align: center; margin: 10px 0;">
    <hr style="border: 5px; height: 20px; width: 100%;">
</div>

### **Helpful Resources for Lab 1**
- For more resources and tutorials on *Bash* scripting, **Markdown**, *Nano*, *Vim*, *Nmap*, and related topics, refer to [Lab 1: Helpful Resources](l1_resources.md).


