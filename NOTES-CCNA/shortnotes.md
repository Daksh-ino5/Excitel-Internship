# CCNA
## SWITCH(Layer-2-Device)
Used for connecting different devices in a network.<br>
  It is a layer 2 device that works on MAC addresses.
  Sends data to only the device specified in the network, it does this using learning the MAC addresses using the CAM table (Content Addressable Memory).<br>
  For eg if SALLY sends a packet to Bob then it will go to bob only no matter how many other devices are connected in the network.<br>
  ## NOTE:<br>
  For checking the devices are up or not we use the ping command.
## HUB:(Layer-3-Device)<br>
When a device sends data to the hub, the hub broadcasts that data to all the connected device,regardless of the specified distination.<br>
Every device on the network will recieve the data but the one intended for the destination will only process it.
## ROUTERS:(Layer-3-Device)
A device used to send and recive data between different networks and uses ip addresses to make decisions.
### Step-by-step:
<li>A device (e.g., your phone) sends data to an external server (e.g., YouTube).
<li>The data packet reaches your home router.
<li>The router checks the destination IP.
<li>Based on its routing table, the router forwards the packet to the next hop (ISP, internet backbone, etc.).
<li>The packet hops through multiple routers until it reaches the destination.<br>

## TCP/IP:<br>
### (Transmission Control Protocol/Internet Protocol)<br>
it is a set of rules or protocols that defines how the data will be sent , recieved , indented etc.
### 4-Layer Model

| Layer               | Function                             | Protocols/Examples         |
|---------------------|--------------------------------------|----------------------------|
| Application         | Interface for apps & users           | HTTP, FTP, DNS, SMTP       |
| Transport           | Manages data transfer                | TCP, UDP                   |
| Internet            | Chooses best path to destination     | IP, ICMP, ARP              |
| Network Access (Link) | Handles actual hardware-level transmission | Ethernet, Wi-Fi, MAC |

### OSI Model – 7 Layers Model<br>

| Layer No. | Layer Name            | Function Summary                                      | Protocols/Examples                      |
|-----------|-----------------------|--------------------------------------------------------|------------------------------------------|
| 7         | Application Layer     | Provides services to the end user (UI interaction)     | HTTP, FTP, SMTP, DNS, Telnet             |
| 6         | Presentation Layer    | Data translation, encryption, compression              | SSL/TLS, JPEG, ASCII, MPEG               |
| 5         | Session Layer         | Manages sessions between applications                  | NetBIOS, RPC, PPTP                       |
| 4         | Transport Layer       | Ensures reliable delivery, error checking              | TCP, UDP                                 |
| 3         | Network Layer         | Routing, addressing (logical IP), path selection       | IP, ICMP, ARP, OSPF, RIP                 |
| 2         | Data Link Layer       | MAC addressing, framing, error detection               | Ethernet, PPP, Switches, MAC addresses   |
| 1         | Physical Layer        | Transmits raw bits over physical media (cables/signals)| Cables, Hubs, Wi-Fi, Bluetooth, Fiber    |
<br>

#  Important Networking Protocols – Quick Notes
<br> There are a total of 65,535 possible port numbers available. These are identified by a 16-bit unsigned integer, meaning they range from 0 to 65,535. 

| Protocol | Full Form                       | Purpose                                      | Port |
|----------|----------------------------------|----------------------------------------------|------|
| **HTTP** | HyperText Transfer Protocol      | Loads web pages (insecure)                   | 80   |
| **HTTPS**| HyperText Transfer Protocol Secure | Loads secure/encrypted web pages (SSL/TLS) | 443  |
| **FTP**  | File Transfer Protocol           | Transfers files between computers            | 21   |
| **SFTP** | SSH File Transfer Protocol       | Secure file transfer using SSH               | 22   |
| **SMTP** | Simple Mail Transfer Protocol    | Sends emails                                 | 25 / 587 |
| **IMAP** | Internet Message Access Protocol | Reads emails while keeping them on server    | 143 / 993 |
| **POP3** | Post Office Protocol v3          | Downloads emails and removes from server     | 110 / 995 |
| **DNS**  | Domain Name System               | Converts domain names to IP addresses        | 53   |
| **DHCP** | Dynamic Host Configuration Protocol | Assigns IPs to devices automatically      | 67 / 68 |
| **TCP**  | Transmission Control Protocol    | Reliable, ordered, connection-based delivery | —    |
| **UDP**  | User Datagram Protocol           | Fast, connectionless, no delivery guarantee  | —    |


# Real-Life Example of OSI Layers  
## Scenario: Sending "Hello" on WhatsApp

### 7. Application Layer  
You open WhatsApp and type "Hello". This layer is where applications like WhatsApp, Gmail, or browsers operate. It provides an interface for user interaction and decides how to send data. WhatsApp uses its own protocol over HTTP/S to communicate.

### 6. Presentation Layer  
The text "Hello" is encoded in a standard format like UTF-8 and encrypted using end-to-end encryption. This layer handles data format translation, encryption, and compression, ensuring both sender and receiver understand the data.

### 5. Session Layer  
WhatsApp sets up and maintains a communication session between you and your friend. This layer controls dialogues (sessions), managing start, duration, and end of data communication.

### 4. Transport Layer  
The message is broken into smaller chunks (segments). The transport layer assigns port numbers to help the system understand which app the data belongs to. TCP ensures the message is delivered reliably and in the correct order.

### 3. Network Layer  
Each segment is placed into a packet and assigned IP addresses of the source (your device) and destination (WhatsApp server or your friend’s device). This layer decides the best path through the network to deliver the message.

### 2. Data Link Layer  
The packet is converted into frames and given MAC addresses (hardware identifiers) of your device and the next device in the network path (like the router). It ensures error detection and delivery on the local network.

### 1. Physical Layer  
The data is converted into electrical signals, radio waves, or light pulses and physically transmitted through Wi-Fi, mobile data, or cables. This layer includes all hardware like your Wi-Fi card, Ethernet cables, and antennas.

# Traditional Data Center Topology (Before)

## Architecture: Three-Tier Network Model  
This was the standard design for enterprise data centers.

### 1. Core Layer (Layer 3 - Routing)  
- Acts as the backbone of the network.  
- Connects multiple distribution switches.  
- Handles high-speed Layer 3 routing across the data center.

### 2. Distribution Layer (Layer 2/3 - Aggregation)  
- Aggregates traffic from access layer switches.  
- Performs Layer 2 switching or Layer 3 routing.  
- Applies policies like filtering and access control.

# Modern Data Center Topology: Leaf-Spine Architecture

## Architecture: Two-Tier Model  
A flat, scalable, and high-performance design used in cloud-scale data centers.

### 1. Spine Switches (Layer 3 - Core)  
- High-speed, non-blocking switches.  
- Every leaf switch connects to all spine switches.  
- Handles fast Layer 3 forwarding.

### 2. Leaf Switches (Layer 2/3 - Access)  
- Connect to servers, storage, and firewalls.  
- Also connect upward to all spine switches.  
- Can perform Layer 2 switching or Layer 3 routing.


### 3. Access Layer (Layer 2 - Switching)  
- Connects end devices like servers and computers.  
- Uses Layer 2 switching, VLANs, and STP.  
- Sometimes supports Layer 3 for advanced setups.


