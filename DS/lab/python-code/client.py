# Import socket module
import socket

# Create a socket object (i.e : sk)
sk = socket.socket()

# initialize port number
port = 5000

# connect to  server on local host
sk.connect(('127.0.0.1', port))
while True:
    expression = input("Enter expression in a * c format with spaces: ")
    sk.send(expression.encode())
    result = sk.recv(1024).decode()  # receiving the result in bytes format.
    print("The result is: ", result)
# close the connection
    sk.close()