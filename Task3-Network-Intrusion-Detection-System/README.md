##### **#Network Intrusion Detection System using Snort**



###### **Overview:**

This project demonstrates the setup and configuration of a Network Intrusion Detection System (NIDS) using Snort on Kali Linux. The objective of this project is to monitor network traffic, detect suspicious or malicious activities, and generate alerts in real-time.



###### **Objectives:**

* Install and configure Snort on Kali Linux
* Monitor network traffic continuously
* Detect suspicious activities using custom rules
* Generate alerts for malicious or unusual traffic
* Improve network security monitoring



###### **Tools \& Technologies:**

* Kali Linux
* Snort
* VirtualBox
* Command Line Interface (CLI)



###### **Installation \& Setup:**

1. Updated Kali Linux system packages
2. Installed Snort using package manager
3. Verified Snort installation
4. Configured network interface
5. Created custom detection rules in local.rules
6. Started Snort for live network monitoring



###### **Custom Rules Configured:**

* **ICMP Ping Detection**

&#x20;  Detects ICMP ping requests in network traffic.

* **SSH Access Detection**

&#x20;  Detects SSH connection attempts on port 22.

* **HTTP Traffic Detection**

&#x20;  Detects HTTP traffic on port 80.

* **HTTPS Traffic Detection**

&#x20;  Detects HTTPS traffic on port 443.



###### **Detection \& Alerts:**

Snort successfully detected:

* ICMP Ping Traffic
* SSH Access Attempts
* HTTP Traffic
* HTTPS Traffic

Real-time alerts were generated whenever suspicious or monitored traffic was detected.



###### **Output:**

The system successfully monitored network traffic and generated alerts based on predefined rules. This confirms that Snort was properly configured and functioning as a Network Intrusion Detection System.



###### **Conclusion:**

This project successfully implemented a Network Intrusion Detection System using Snort in Kali Linux. The configured rules effectively detected different types of network activities and generated alerts in real time. This project improved understanding of intrusion detection and network security monitoring.

