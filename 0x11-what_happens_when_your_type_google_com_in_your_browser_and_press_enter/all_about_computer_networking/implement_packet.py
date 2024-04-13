import socket

def packet_filter(packet):
    # Implement packet filtering logic here
    # For demonstration purposes, allow all packets
    return True

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Accept incoming connection
        connection, client_address = server_socket.accept()

        try:
            print('Connection established with', client_address)

            # Receive data
            data = connection.recv(1024)
            print('Received:', data.decode())

            # Packet filtering
            if packet_filter(data):
                # Allow packet
                connection.sendall(b'Packet allowed by firewall')
            else:
                # Block packet
                connection.sendall(b'Packet blocked by firewall')

        finally:
            # Close connection
            connection.close()

if __name__ == '__main__':
    main()

