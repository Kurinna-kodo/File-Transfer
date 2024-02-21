import socket
import os
import ssl

def send_file(file_name, host, port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Create an SSL context for secure communication
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    
    # Wrap the socket with SSL for encryption
    secure_socket = context.wrap_socket(client_socket, server_hostname=host)
    
    try:
        # Establish a secure connection to the server
        secure_socket.connect((host, port))
        print(f"Connected securely to {host} on port {port}")
        
        # Get the size of the file to be sent
        file_size = os.path.getsize(file_name)
        
        # Send metadata (file name and size) to the server
        secure_socket.send(f"{file_name}, {file_size}".encode('utf-8'))
        
        # Open the file and send its contents to the server
        with open(file_name, 'rb') as file:
            # Read and send the file in chunks to manage memory usage efficiently
            data = file.read(4096)
            while data:
                secure_socket.sendall(data)
                data = file.read(4096)

        print(f"File {file_name} has been sent securely.")
    except Exception as e:
        print(f"Failed to send file securely: {e}")
    finally:
        # Close the secure connection
        secure_socket.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python client.py <filename> <server_host> <server_port>")
        sys.exit(1)
    filename = sys.argv[1]
    server_host = sys.argv[2]
    server_port = int(sys.argv[3])
    
    send_file(filename, server_host, server_port)



