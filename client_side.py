import socket
import os

def send_file(file_name, host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    #Get file size
    file_size = os.path.getsize(file_name)

    #Send the file name and size as metadata
    client_socket.send(f"{file_name}, {file_size}".encode('utf-8'))

    #Send the file data
    with open(file_name, 'rb') as file:
        client_socket.sendfile(file,0)

    print(f"File {file_name} has been sent.")
    client_socket.close()

    


