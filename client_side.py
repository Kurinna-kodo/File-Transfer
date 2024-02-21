import socket
import os
import ssl
import json
import threading

def send_file(file_names, host, port):

    for file_name in file_names:
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
            
            #Create Metadata Dictionary and convert to JSON
            metadata = [{'file_name': file_name, 'file_size': os.path.getsize(file_name)} for file_name in file_names]
            metadata_json = json.dumps(metadata)

            # Send metadata (file name and size) to the server
            secure_socket.send(metadata_json.encode('utf-8'))
            
            # Open the file and send its contents to the server
            with open(file_name, 'rb') as file:
                # Read and send the file in chunks to manage memory usage efficiently
                data = file.read(4096)
                while data:
                    secure_socket.sendall(data)
                    data = file.read(4096)

            print(f"File {file_name} has been sent securely.")
        except Exception as e:
            print(f"Failed to send file {file_name} securely: {e}")
        finally:
            # Close the secure connection
            secure_socket.close()

def send_files(file_names, host, port):
    #create a thread for each file to be sent
    threads = []
    for file_name in file_names:
        thread = threading.Thread(target=send_file, args=([file_name], host, port))
        threads.append(thread)
        thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename1> [<filename2> ...]")
        sys.exit(1)
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    file_names = sys.argv[3:]
    
    send_files(file_names, server_host, server_port)



