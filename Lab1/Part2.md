## **Part 2: CTI Training with MITRE ATT&CK**

### Mapping (5 Behaviors)

#### **Behavior **
##### **Document Your Findings**
---
[*Cutting Edge APT Campaign: 2023–2024 Cyber Espionage Targeting ICS Vulnerabilities*](CuttingEdge_APT_report.html).
- **Behavior 1:**   
Using **CVE-2023-46805** the adversary sent malformed HTTP requests and forged authentication tokens to bypass the authentication mechanism, gaining access while appearing to be a legitimate user.   
- **Mapping Process**:
- **Tactic(why?):**   
Objective: Initial Access   
Adversary gains unauthorized entry while bypassing authentication control on an internet-facing host 
- **Technique:**    
ID: **T1190 - Exploit Public-Facing Application**   
  - Sub-Technique: NONE
- **Justification:**
The report found that the combination of malformed HTTP requests and forged authentication tokens was used to make it appear that legitimate users were accessing the system. In ATT&CK, this aligns with T1190, which involves exploiting a weakness in a public-facing application. The mapping covers adversaries exploiting vulnerabilities in Internet host applications to achieve unauthorized acces
---

[*CICD-SEC-4: Poisoned Pipeline Execution (PPE)*](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution)
- **Behavior 2**:
The attacker abused source-control permissions, modified a CI pipeline configuration to run malicious commands, stole AWS credentials during pipeline execution, and then used those credentials to access the production cloud environment
- **Mapping Process**:
  1. **Tactic**:  
   Objective:**Execution**  
  2. **Technique**: **T1082 - Poisoned Pipeline Execution**  
     - Sub-Technique: NONE
  3. **Justification**:  
  The attacker manipulated the CI/CD pipeline so that malicious commands were executed automatically as part of the build process. This directly aligns with Poisoned Pipeline Execution, which describes injecting malicious logic into CI/CD workflows to execute attacker-controlled code.
---

[*Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware*](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- **Behavior 3**:
The attackers performed system information discovery to gather details about the operating system and hardware configuration using system utilities and APIs. The collected information was then used to inform and tailor future attack actions.
- **Mapping Process**:
  1. **Tactic**: **Discovery**
  2. **Technique**: **T1082- System Information Discovery**
     - Sub-Technique: NONE
  3. **Justification**:  
 I selected techniques because the attackers get informed before an attack. The techniques aligned with the behavior because the attacker is gathering information about the system configuration. Tactics align with behavior because the information about the system configuration is collected
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
While initally I thought the tactic from WARPWIRE was Lateral Movement, Credential Access would be the correct tactic. WARPWIRE enabled but did not directly do Lateral Movement. From its actions of intercepting and exfiltration it was able to do Credential Access from captured ICS web interfaces, capturing web portal login credentials input. This was done through a web portal.
---

[Backdoor Persistence through Server Software Modification]()
 - **Behavior 5**:
PITHOOK hooked critical web server functions within ICS appliances to establish and maintain a persistent backdoor.
- **Mapping Process**:
  1. **Tactic**: **Persistence**
   Objective:**The adversary is trying to maintain their foothold through consistent backdoor access.**  
  2. **Technique**: **T1505 - Server Software Component**  
     - Sub-Technique: NONE
  3. **Justification**:
The goal of PITHOOK was to maintain a consistent backdoor access using web server functions, BASE64 and AES, that are commonly used for enterprise server applications aligning with T1505. So we know the main tactic is persistence and Server Software Component would be the technique as  the goal is to extend and abuse these enterprise server applications.
---

Example 1: Achieving Persistence Through Malware Deployment

Behavior:
Attackers deployed the ZIPLINE backdoor, which embedded itself into core system libraries like libsecure.so, hijacked incoming traffic, and triggered malicious operations such as reverse shell activation and file transfers.
Mapping Process:
Tactic: Persistence
Objective: Maintain long-term access to the system.
Technique: T1547 - Boot or Logon Autostart Execution
Sub-Technique: T1547.001 - Registry Run Keys/Startup Folder
Justification:
ZIPLINE altered system startup files to maintain persistence across reboots. The use of core library modification aligns with the Persistence tactic and Boot or Logon Autostart Execution technique, ensuring consistent access to the compromised system.