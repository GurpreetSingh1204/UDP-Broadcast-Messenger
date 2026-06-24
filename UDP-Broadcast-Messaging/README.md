# UDP Broadcast Messaging

A simple Python-based UDP broadcast messaging application that allows devices connected to the same network to send and receive messages using the UDP protocol.

---

## Features

* Broadcast messages to all devices in the local network.
* Lightweight implementation using Python's built-in `socket` module.
* No external libraries required.
* Real-time message delivery.
* Suitable for networking and cybersecurity learning projects.

---

## Project Structure

```
UDP-Broadcast-Messaging/
│
├── sender.py
├── receiver.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Requirements

* Python 3.8 or later
* Devices connected to the same LAN, Wi-Fi, or PAN network

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/UDP-Broadcast-Messaging.git
```

Move into the project directory:

```bash
cd UDP-Broadcast-Messaging
```

---

## Running the Receiver

```bash
python receiver.py
```

Output:

```
Waiting for messages...
```

---

## Running the Sender

```bash
python sender.py
```

Example:

```
Enter message: Hello Network
```

Receiver Output:

```
From ('192.168.1.10', 5000): Hello Network
```

---

## How It Works

1. The sender creates a UDP socket.
2. Broadcast mode is enabled.
3. The message is transmitted to `255.255.255.255`.
4. Any receiver listening on port 5000 receives the message.

---

## Protocol Used

* UDP (User Datagram Protocol)
* IPv4 Broadcast Address: `255.255.255.255`
* Port: `5000`

---

## Applications

* LAN chat systems
* Broadcast notification systems
* Device discovery
* IoT communication
* Networking and cybersecurity experiments

---

## Future Improvements

* Multiple clients support
* GUI using Tkinter
* Timestamped messages
* Username support
* Encryption with AES
* File transfer capability

---

## Author

Gurpreet Singh

Master of Computer Applications (Cybersecurity)

---

## License

MIT License
