import socket

PORT = 5000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Listen on port 5000
sock.bind(('', PORT))

print("Waiting for messages...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"From {addr}: {data.decode()}")
