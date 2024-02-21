README.md

# File Transfer Project

## Overview
This project is a simple file transfer application using Python's socket programming. It consists of a server script (`server.py`) that listens for incoming files and a client script (`client.py`) that sends files to the server. The goal is to demonstrate basic network programming concepts, file handling, and client-server communication in Python.

## Features
- File transfer over TCP/IP protocol.
- Simple server and client script setup.
- Server accepts and saves incoming files.
- Client sends files with metadata (name and size).

## Setup and Running

### Prerequisites
- Python 3.6 or higher installed on your machine.
- Basic knowledge of socket programming in Python.

### Installation
1. Clone this repository to your local machine using `git clone https://github.com/Kurinna-kodo/File-Transfer.git
2. Navigate to the `file_transfer` directory.

### Running the Application
1. **Start the server:** 
   - Run `python server.py` in your terminal. The server will start listening for incoming connections.
2. **Send a file from the client:** 
   - Open a new terminal session, navigate to the `file_transfer` folder.
   - Run `python client.py <filename> <server_host> <server_port>`, replacing `<filename>`, `<server_host>`, and `<server_port>` with the appropriate values. This sends the specified file to the server.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for more details.

## Contact
- Alex Rozovsky - [alexrozovsky1@gmail.com](mailto:alexrozovsky1@gmail.com)

Project Link: https://github.com/Kurinna-kodo/File-Transfer.git
