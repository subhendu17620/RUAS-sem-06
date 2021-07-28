# first of all import the socket library
import socket

def calcy(expression):
    a,op,c=expression.split()
    a=float(a)
    c=float(c)
    if(op=='+'): 
        return a+c
    elif(op=='-'):
        return a-c
    elif(op=='/'):
        return a/c
    elif(op=='*'):
        return a*c

# next create a socket object
s = socket.socket()
print("Socket successfully created")

port = 5000
s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")


while True:

    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    while True:
        expression = c.recv(1024).decode()    # receiving the expression form client.
        result = calcy(expression)  # calling calcy function
        c.send(str(result).encode())

    # Close connection
    c.close()