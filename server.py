import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind(("127.0.0.1", 12345))

# Listen for incoming connections
s.listen(5)

while True:
    # Establish a connection
    c, addr = s.accept()
    print("Got connection from", addr)
    try:
        # Open the file to be sent
        with open("image.png", "rb") as f:
            # Read the file into a variable
            data = f.read()
    except FileNotFoundError:
        print("File not found")
    else:
        # Send the total size of the image in bytes
        total_size = len(data)
        c.sendall(str(total_size).encode())
        # Send the file to the client
        c.sendall(data)
        print("File sent successfully")

    # Close the connection
    c.close()
