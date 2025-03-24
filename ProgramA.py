#IT3883/W02
#Nornu Ninayor
#Assignment 3
#03/24/25
#Prompts the user for input, sends it to Program B, and prints the response.
#Resources used W3chool,youtube,& google,github


import socket  # This allows communication between two programs.

HOST = '127.0.0.1'  # Localhost (this computer)
PORT = 45000        # Chosen port number to connect to Program B

# Create a socket (like picking up the phone)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to Program B (call it)

    # Ask user to type something
    message = input("Enter a string to send to Program B: ")

    # Send message to Program B
    s.sendall(message.encode())

    # Wait for Program B's response
    data = s.recv(1024)  # Receive up to 1024 bytes of data

    # Print what was received
    print('Received from Program B:', data.decode())
