import os
import socket
import ssl

def receive_file(secure_socket):
    print("Connection has been established.")

    # Accept the header with file name and file size
    file_info = secure_socket.recv(1024).decode('utf-8')
    file_name, file_size = file_info.split(',')
    file_size = int(file_size)

    # Open the file and write it in binary mode
    with open(file_name, 'wb') as file:
        bytes_received = 0
        while bytes_received < file_size:
            chunk = secure_socket.recv(min(4096, file_size - bytes_received))
            if not chunk:
                break  # Close connection if no more data
            file.write(chunk)
            bytes_received += len(chunk)

    print(f'File {file_name} has been received.')
    secure_socket.close()  # Ensure the secure socket is closed properly

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()
    print("Server is listening on 127.0.0.1:5000...")

    # Create an SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Attempt to load the server's certificate and private key from environment variables
    certfile = os.getenv('MY_APP_CERT_FILE')
    keyfile = os.getenv('MY_APP_KEY_FILE')

    try:
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    except Exception as e:
        print(f"Failed to load SSL certificate/key: {e}")
        exit(1)  # Exit the program if the certificate/key cannot be loaded

    while True:
        # Accept new connections
        client_socket, addr = server_socket.accept()
        print(f"Connection attempt from {addr}")

        try:
            # Secure the connection
            secure_socket = context.wrap_socket(client_socket, server_side=True)
            receive_file(secure_socket)
        except Exception as e:
            print(f"Error securing connection: {e}")
            client_socket.close()

if __name__ == "__main__":
    start_server()
