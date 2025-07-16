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
###(Transmission Control Protocol/Internet Protocol)<br>
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


