import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(("127.0.0.1", 12345))

# Receive the file from the server
try:
    total_size = int(s.recv(1024).decode())
    received_size = 0
    with open("received_image.png", "wb") as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
            received_size += len(data)
            print(f'\r{(received_size / total_size) * 100}% downloaded', end='', flush=True)
except:
    print("Error receiving file")
else:
    print("\nFile received successfully")

# Close the connection
s.close()
