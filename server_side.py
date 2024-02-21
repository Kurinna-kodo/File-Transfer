import os
import socket
import ssl
import json
import threading
import hashlib
import logging

# Configure logging
logging.basicConfig(filename='server.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

def calculate_file_hash(file_name):
    hasher = hashlib.sha256()
    with open(file_name, 'rb') as file:
        buffer = file.read(65536)  # Read the file in chunks to conserve memory
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(65536)
    return hasher.hexdigest()

def receive_file(secure_socket, metadata):
    # Extract file name, size, and hash from metadata dictionary
    file_name = metadata['file_name']
    file_size = metadata['file_size']
    file_hash = metadata['file_hash']

    # Open the file and write it in binary mode
    with open(file_name, 'wb') as file:
        bytes_received = 0
        while bytes_received < file_size:
            chunk = secure_socket.recv(min(4096, file_size - bytes_received))
            if not chunk:
                break  # Close connection if no more data
            file.write(chunk)
            bytes_received += len(chunk)

    # Calculate the hash of the received file
    received_file_hash = calculate_file_hash(file_name)

    # Verify the received file hash
    if received_file_hash == file_hash:
        logging.info(f'File {file_name} has been received and verified.')
        print(f'File {file_name} has been received and verified.')
    else:
        logging.error(f'File {file_name} has been received, but verification failed.')
        print(f'File {file_name} has been received, but verification failed.')
        secure_socket.close()  # Terminate the connection if verification fails
        return

    print(f'File {file_name} has been received.')
    secure_socket.close()  # Ensure the secure socket is closed properly

def handle_client(secure_socket):
    try:
        metadata_json = secure_socket.recv(1024).decode('utf-8')
        metadata = json.loads(metadata_json)
        receive_file(secure_socket, metadata)
    except Exception as e:
        logging.error(f"Error handling client: {e}")
        print(f"Error handling client: {e}")
    finally:
        secure_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5001))
    server_socket.listen()
    print("Server is listening on 127.0.0.1:5001...")

    # Create an SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Attempt to load the server's certificate and private key from environment variables
    certfile = os.getenv('MY_APP_CERT_FILE')
    keyfile = os.getenv('MY_APP_KEY_FILE')

    try:
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    except Exception as e:
        logging.error(f"Failed to load SSL certificate/key: {e}")
        print(f"Failed to load SSL certificate/key: {e}")
        exit(1)  # Exit the program if the certificate/key cannot be loaded

    # Specify the path to the file containing trusted CA certificates
    cafile = 'path/to/cafile.pem'

    # Load the trusted CA certificates
    context.load_verify_locations(cafile=cafile)

    while True:
        # Accept new connections
        client_socket, addr = server_socket.accept()
        print(f"Connection attempt from {addr}")

        try:
            # Secure the connection
            secure_socket = context.wrap_socket(client_socket, server_side=True)

            client_handler = threading.Thread(target=handle_client, args=(secure_socket,))
            client_handler.start()

        except Exception as e:
            logging.error(f"Error securing connection: {e}")
            print(f"Error securing connection: {e}")
            client_socket.close()

if __name__ == "__main__":
    start_server()
