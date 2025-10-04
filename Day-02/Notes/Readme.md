# Networking Concepts: OSI Model, TCP/IP, Media, IEEE Standards, Ping, Wireless Networks, and IP Addressing

## OSI Model (Open Systems Interconnection)
The OSI model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers.

### Seven Layers of OSI Model

1. **Application Layer**
   - **Function:** Provides network services to user applications
   - **Protocols:** HTTP, FTP, SMTP, DNS, Telnet
   - **Devices:** Gateways
   - **Data Unit:** Message

2. **Presentation Layer**
   - **Function:** Data translation, encryption, compression
   - **Protocols:** SSL/TLS, JPEG, MPEG, ASCII
   - **Data Unit:** Message

3. **Session Layer**
   - **Function:** Establishes, manages, and terminates connections
   - **Protocols:** NetBIOS, PPTP, RPC
   - **Data Unit:** Message

4. **Transport Layer**
   - **Function:** End-to-end connection, reliability, flow control
   - **Protocols:** TCP, UDP, SCTP
   - **Data Unit:** Segment (TCP) / Datagram (UDP)

5. **Network Layer**
   - **Function:** Logical addressing, routing, path determination
   - **Protocols:** IP, ICMP, IPsec, OSPF, BGP
   - **Devices:** Routers
   - **Data Unit:** Packet

6. **Data Link Layer**
   - **Function:** Physical addressing, error detection, frame synchronization
   - **Protocols:** Ethernet, PPP, HDLC, VLAN
   - **Devices:** Switches, Bridges, NICs
   - **Data Unit:** Frame
   - **Sub-layers:**
     - LLC (Logical Link Control)
     - MAC (Media Access Control)

7. **Physical Layer**
   - **Function:** Physical connection, bit transmission
   - **Protocols:** RS-232, 100Base-TX, DSL
   - **Devices:** Hubs, Repeaters, Cables
   - **Data Unit:** Bit

---

## TCP/IP Model
The TCP/IP model is a practical implementation model used in real-world networking.

### Four Layers of TCP/IP Model

1. **Application Layer**
   - Combines OSI Application, Presentation, and Session layers
   - **Protocols:** HTTP, FTP, SMTP, DNS, SNMP

2. **Transport Layer**
   - Same as OSI Transport Layer
   - **Protocols:** TCP, UDP

3. **Internet Layer**
   - Equivalent to OSI Network Layer
   - **Protocols:** IP, ICMP, ARP

4. **Network Access Layer**
   - Combines OSI Data Link and Physical layers
   - **Protocols:** Ethernet, Wi-Fi, PPP

### Key Differences Between OSI and TCP/IP

| Feature             | OSI Model                | TCP/IP Model          |
|--------------------|-------------------------|---------------------|
| Layers             | 7 layers                | 4 layers            |
| Development        | Theoretical model       | Practical implementation |
| Protocol Dependency| Protocol independent    | Protocol dependent  |
| Approach           | Top-down                | Bottom-up           |
| Usage              | Reference model         | Actual implementation |

---

## Explanation of Different Types of Media

### Guided Media (Wired)

1. **Twisted Pair Cable**
   - Two insulated copper wires twisted together
   - Types:  
     - **UTP (Unshielded Twisted Pair)**: No shielding, Cat5/Cat5e/Cat6/Cat6a/Cat7, max length 100m, low cost  
     - **STP (Shielded Twisted Pair)**: Shielded to reduce EMI, better performance, higher cost

2. **Coaxial Cable**
   - Central conductor surrounded by insulation, shield, and outer jacket
   - Types: Thicknet (10Base5), Thinnet (10Base2), RG-6
   - Applications: Cable TV, broadband internet, Ethernet networks

3. **Fiber Optic Cable**
   - Uses light pulses through glass/plastic fibers
   - Types: Single-mode (long distance, high bandwidth, laser), Multi-mode (short distance, LED)
   - Advantages: High bandwidth, long distance, immune to EMI, secure  
   - Disadvantages: Expensive, fragile, difficult to install

### Unguided Media (Wireless)

1. **Radio Waves**
   - Frequency: 3kHz–300GHz, omnidirectional, penetrates walls
   - Applications: AM/FM radio, TV, Wi-Fi, Bluetooth

2. **Microwaves**
   - Frequency: 300MHz–300GHz, directional, line-of-sight
   - Types: Terrestrial (point-to-point), Satellite (via satellites)

3. **Infrared**
   - Frequency: 300GHz–400THz, short range, line-of-sight
   - Applications: Remote controls, IR data transfer

---

## IEEE Standards Committee and Formats

- **Founded:** 1963
- **Purpose:** Develop standards for technologies
- **Structure:** Various working groups

### Important IEEE Standards

- **IEEE 802 Series (LAN/MAN Standards)**
  - 802.3 - Ethernet (10Base-T, 100Base-TX, 1000Base-T, 10GBase-T)
  - 802.11 - Wireless LAN (Wi-Fi 6, etc.)
- Other Standards: 802.1 (Bridging), 802.2 (LLC), 802.5 (Token Ring), 802.15 (Bluetooth), 802.16 (WiMAX)

### IEEE Standards Format
IEEE XXX.Y-ZAAAAB
│ │ │ │ │ │
│ │ │ │ │ └── Additional specifications
│ │ │ │ └──── Year of publication
│ │ │ └────── Amendment letter
│ │ └──────── Sub-standard number
│ └──────────── Standard number
└────────────────── IEEE identifier



---

## Working of Ping

### What is Ping?
- **Full Form:** Packet Internet Groper  
- **Purpose:** Network diagnostic tool to test connectivity  
- **Protocol Used:** ICMP

### How Ping Works
1. **Command Execution:** `ping <destination_IP_or_hostname>`  
2. **ICMP Echo Request:** Source device sends ICMP Echo Request  
3. **Packet Transmission:** Travels through network  
4. **Destination Processing:** Target device creates Echo Reply  
5. **Reply Transmission:** Echo Reply returns to source  
6. **Source Processing:** RTT calculated and statistics displayed  

### Ping Command Examples
```bash
ping google.com          # Basic ping
ping -c 4 google.com     # Number of packets
ping -s 1000 google.com  # Packet size
ping -t google.com       # Continuous ping
ping -W 5 google.com     # Set timeout
```

### Wireless Network and Internet Authority
Regulatory Bodies
International: ITU, IEEE

United States: FCC

Europe: ETSI

United Kingdom: Ofcom

Wireless Spectrum Allocation
2.4 GHz ISM Band: Wi-Fi, Bluetooth, Zigbee

5 GHz UNII Bands: Wi-Fi, radar

900 MHz ISM Band: Cordless phones, RFID

Internet Governance
ICANN: IP allocation, DNS management

IETF: TCP/IP standards

IANA: IP address management, now part of ICANN

### IP Address in Detailed Explanation
What is an IP Address?
Definition: Numerical label for devices on a network

Purpose: Identification and location addressing

Format: Binary represented in human-readable notation

IP Address Versions
IPv4
Size: 32 bits

Format: Dotted-decimal (192.168.1.1)

Classes: A, B, C, D, E

Subnet Mask Examples:

Class A: 255.0.0.0

Class B: 255.255.0.0

Class C: 255.255.255.0

IPv6
Size: 128 bits

Format: Hexadecimal (2001:0db8::8a2e:0370:7334)

Types: Unicast, Multicast, Anycast

IP Address Components
Network ID: Identifies network segment

Host ID: Identifies specific device

Subnetting
Purpose: Efficient use, segmentation, security

Subnet Mask Example: 255.255.255.0

CIDR Example: 192.168.1.0/24

Special IP Addresses
Private Ranges:

10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

Loopback: 127.0.0.1

Default: 0.0.0.0

Broadcast: 255.255.255.255

APIPA: 169.254.x.x

IP Address Assignment
Static: Manual, consistent

Dynamic: DHCP

APIPA: Auto when DHCP fails

IP Address Example
```bash
IP Address: 192.168.1.100
Subnet Mask: 255.255.255.0
CIDR: 192.168.1.100/24
Network ID: 192.168.1.0
Host ID: 100
Broadcast Address: 192.168.1.255
Usable Host Range: 192.168.1.1 - 192.168.1.254
Total Hosts: 256
Usable Hosts: 254
```