README.md

# File Transfer Project

## Overview
This project is a simple file transfer application using Python's socket programming. It consists of a server script (`server.py`) that listens for incoming files and a client script (`client.py`) that sends files to the server. The goal is to demonstrate basic network programming concepts, file handling, and client-server communication in Python.

## Features
- Secure file transfer over TCP/IP protocol using SSL encryption.
- Simple server and client script setup with SSL support.
- Server accepts and saves incoming files securely.
- Client sends files with metadata (name and size) over an encrypted connection.

## Setup and Running

### Prerequisites
- Python 3.6 or higher installed on your machine.
- OpenSSL to generate SSL certificates for secure communication.
- Basic knowledge of socket programming and SSL in Python.


### Installation
1. Clone this repository to your local machine using `git clone https://github.com/Kurinna-kodo/File-Transfer.git
2. Navigate to the `file_transfer` directory.

### Generating SSL Certificates
Before running the server, generate a self-signed SSL certificate and private key:
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem


### Configuring the Application
Set environment variables for the SSL certificate and private key paths:

#### On Linux/macOS
export MY_APP_CERT_FILE=/path/to/your/certificate.pem
export MY_APP_KEY_FILE=/path/to/your/key.pem


#### On Windows

For Command Prompt:
set MY_APP_CERT_FILE=C:\path\to\your\certificate.pem
set MY_APP_KEY_FILE=C:\path\to\your\key.pem

For PowerShell:
env:MY_APP_CERT_FILE="C:\path\to\your\certificate.pem"
$env:MY_APP_KEY_FILE="C:\path\to\your\key.pem"

### Running the Application
1. **Start the server:** 
   - Ensure the environment variables for the SSL certificate and key paths are set.
   - Run `python server.py` in your terminal. The server will start listening for incoming connections securely.

2. **Send a file from the client:** 
   - Open a new terminal session, navigate to the `file_transfer` folder.
   - Ensure the server's SSL certificate is trusted or available for the client.
   - Run `python client.py <filename> <server_host> <server_port>`, replacing `<filename>`, `<server_host>`, and `<server_port>` with the appropriate values. This sends the specified file to the server securely.

## Contributing
Contributions are greatly appreciated. If you have an idea that would improve this project, follow these steps to contribute:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- Alex Rozovsky - [alexrozovsky1@gmail.com](mailto:alexrozovsky1@gmail.com)

Project Link: [https://github.com/Kurinna-kodo/File-Transfer](https://github.com/Kurinna-kodo/File-Transfer)
