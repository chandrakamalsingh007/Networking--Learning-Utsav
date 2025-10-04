# 📘 Networking Notes

This document provides detailed notes on fundamental networking concepts including **Network, Networking, Internetworking, Types of Networks, Transmission Modes & Mediums, Network Topologies, and Networking Devices**.

---

## 1️⃣ Network, Networking, and Internetworking

### 🔹 Network
- A **network** is a collection of interconnected devices (computers, servers, IoT devices, etc.) that share resources and communicate with each other.
- Purpose:
  - Resource sharing (files, printers, storage)
  - Communication (email, messaging, VoIP)
  - Data transfer
- **Example**: A LAN in a home where multiple devices connect to the same Wi-Fi router.

---

### 🔹 Networking
- **Networking** refers to the process of **designing, configuring, implementing, and managing** a network.
- It involves:
  - Setting up hardware (switches, routers, access points)
  - Configuring software (protocols like TCP/IP, DHCP, DNS)
  - Ensuring **security, performance, and reliability**
- **Example**: Configuring VLANs in a corporate LAN.

---

### 🔹 Internetworking
- **Internetworking** is the practice of connecting multiple different networks together using networking devices.
- The goal is to create a **network of networks** that communicate seamlessly.
- Uses **routers, gateways, and firewalls**.
- **Example**: The Internet is the largest internetwork (billions of devices across the globe).

---

## 2️⃣ Types of Network

### Based on Geographical Area

1. **LAN (Local Area Network)**
   - Covers small area (home, office, school).
   - High speed (up to 10 Gbps), low cost.
   - Owned privately.
   - **Example**: Office Wi-Fi network.

2. **MAN (Metropolitan Area Network)**
   - Covers a city or metropolitan area.
   - Higher cost than LAN.
   - Often maintained by ISPs or government bodies.
   - **Example**: Cable TV networks in a city.

3. **WAN (Wide Area Network)**
   - Covers large geographical areas (countries, continents).
   - Uses satellite links, leased lines, optical fiber.
   - **Example**: The Internet.

4. **PAN (Personal Area Network)**
   - Very small range (usually within 10 meters).
   - Used for connecting personal devices.
   - **Example**: Bluetooth, Hotspot.

5. **CAN (Campus Area Network)**
   - Covers multiple LANs within a campus environment.
   - **Example**: University or hospital campus network.

---

### Based on Functionality

1. **Client-Server Network**
   - Centralized server provides services (authentication, file storage).
   - Easier to manage and secure.

2. **Peer-to-Peer (P2P) Network**
   - No dedicated server; all devices share resources equally.
   - Low cost, less secure, suited for small networks.

---

## 3️⃣ Transmission Modes and Mediums

### 🔹 Transmission Modes (Direction of Data Flow)

1. **Simplex**
   - One-way communication only.
   - Example: Keyboard → Computer.

2. **Half Duplex**
   - Two-way communication but **one direction at a time**.
   - Example: Walkie-talkie.

3. **Full Duplex**
   - Two-way communication simultaneously.
   - Example: Telephone conversation.

---

### 🔹 Transmission Mediums (How data travels)

#### 1. Guided Media (Wired)
- **Twisted Pair Cable**  
  - Common in Ethernet LANs (Cat5, Cat6).
  - Inexpensive, limited distance.  

- **Coaxial Cable**  
  - Used in older TV networks, CCTV.  
  - Good noise immunity.  

- **Optical Fiber**  
  - High bandwidth, long distance.  
  - Immune to electromagnetic interference.  
  - Used in ISPs, backbone connections.  

#### 2. Unguided Media (Wireless)
- **Radio Waves** → Wi-Fi, FM radio.  
- **Microwaves** → Satellite links, long-distance backhaul.  
- **Infrared** → TV remotes, short-range.  
- **Satellite Communication** → GPS, global broadcasting.  

---

## 4️⃣ Network Topologies

Network topology defines the **arrangement of nodes and connections** in a network.

1. **Bus Topology**
   - All devices share a single backbone cable.
   - Cheap but backbone failure → entire network fails.

2. **Star Topology**
   - All devices connected to a central switch/hub.
   - Easy to troubleshoot, scalable.
   - Central device failure = network down.

3. **Ring Topology**
   - Devices connected in a closed loop.
   - Data travels in one direction.
   - Failure of one node can impact network.

4. **Mesh Topology**
   - Each device connects to every other device.
   - Very reliable (multiple paths).
   - Expensive and complex.

5. **Tree Topology**
   - Hierarchical combination of star and bus.
   - Suitable for large organizations.

6. **Hybrid Topology**
   - Mix of two or more topologies.
   - Example: Star + Mesh in data centers.

---

## 5️⃣ Networking Devices

1. **Hub**
   - Layer 1 device (Physical Layer).
   - Broadcasts data to all devices.
   - Inefficient, rarely used today.

2. **Switch**
   - Layer 2 device (Data Link Layer).
   - Forwards frames based on **MAC addresses**.
   - Provides better efficiency than hubs.

3. **Router**
   - Layer 3 device (Network Layer).
   - Routes packets based on **IP addresses**.
   - Connects multiple networks (LAN to WAN).

4. **Access Point (AP)**
   - Provides **wireless connectivity** to wired LAN.

5. **Gateway**
   - Connects networks using different protocols.
   - Example: PSTN (phone) to VoIP gateway.

6. **Modem**
   - Converts digital signals ↔ analog signals.
   - Used in DSL/broadband internet.

7. **Firewall**
   - Filters incoming/outgoing traffic based on rules.
   - Provides network security.

8. **Repeater**
   - Regenerates signals to extend network distance.

---

## 📌 Summary

- **Network** = Collection of devices.  
- **Networking** = Process of building & managing networks.  
- **Internetworking** = Connecting multiple networks together.  
- **Types of Networks** = LAN, WAN, MAN, PAN, CAN.  
- **Transmission** = Simplex, Half Duplex, Full Duplex + guided/wireless mediums.  
- **Topologies** = Bus, Star, Ring, Mesh, Tree, Hybrid.  
- **Devices** = Hub, Switch, Router, AP, Gateway, Modem, Firewall, Repeater.  

---
