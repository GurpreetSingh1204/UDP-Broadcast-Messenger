import socket

PORT = 5000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = input("Enter message: ")

# Send message to all devices in network
sock.sendto(message.encode(), ('255.255.255.255', PORT))
