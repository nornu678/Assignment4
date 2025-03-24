#IT3883/W02
#Nornu Ninayor
#Assignment 4
#03/24/25
#Resources used W3chool,youtube,& google,lecture notes, github
#Purpose: Listens for a message from Program A, converts it to uppercase, and sends it back.


import socket  # This allows communication between two programs.

HOST = '127.0.0.1'  # Localhost (this computer)
PORT = 45000        # Chosen port number to listen on

# Create a socket (like setting up a phone to receive calls)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind to the address
    s.listen()  # Start listening for connections
    print(f'Program B is listening on {HOST}:{PORT}')

    # Accept a connection from Program A
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        # Receive message from Program A
        data = conn.recv(1024)
        if data:
            print('Received from Program A:', data.decode())

            # Convert message to uppercase
            response = data.decode().upper()

            # Send back uppercase message
            conn.sendall(response.encode())
