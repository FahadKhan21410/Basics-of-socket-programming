# Basics-of-socket-programming
This project demonstrates how a TCP server and client can communicate with each other using Python’s socket module.

* The server:
  * Uses multi-threading to handle multiple clients simultaneously.
  * Listens for incoming connections and prints out client messages.
  * Cleanly disconnects clients when the "Disconnect" message is received.

* The client:
  * Connects to the server via TCP.
  * Sends encoded messages with a fixed-size header (for message length).
  * Gracefully disconnects when instructed.

## Features
* Custom message framing using a fixed header size (64 bytes).
* Multi-threaded server to support multiple client connections.
* Example message exchange between server and client.

## Technology
* Python (Socket,Threading)

## Development Environment
* PyCharm

## Project Structure
* /server.py   -> Handles incoming client connections, receives messages, manages threads
* /client.py   -> Connects to the server, sends messages, and disconnects gracefully

## How To Run
* Clone repository (bash: git clone https://github.com/username/project.git) or Download as ZIP
* Open the code file in IDE that supports python
* First run the server.py then the client.py

## Demo
* https://youtu.be/bpdgPMg5ZSU (How the code works)

## License
* This project is licensed under the MIT License - see the [LICENSE] file for details.


