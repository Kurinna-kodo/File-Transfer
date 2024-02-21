import socket

def receive_file(server_socket):
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")

    #Accept the header w/ file name and file size
    file_info = client_socket.recv(1024)
    file_name, file_size = file_info.decode('utf-8').split(',')
    file_size = int(file_size)

    # Open the file and write it in binary mode
    with open(file_name, 'wb') as file:
        #initialize counter
        bytes_received = 0
        while bytes_received < file_size:
            chunk = client_socket.recv(min(4096, file_size - bytes_received))
            if not chunk:
                break #Close connection
            file.write(chunk)
            bytes_received += len(chunk)

    print(f'File {file_name} has been received.')
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()
    print("Server is listening..")

    while True:
        receive_file(server_socket)

start_server()