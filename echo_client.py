#!/usr/bin/python
# A script to send a message to an Echo server
# and print the response

import socket
import sys

def print_useage():
    print("A Python Echo client.")
    print("Useage:")
    print("python echo_client.py <<IP ADDRESS>> <<PORT>> message")
    print("i.e. python echo_client.py 127.0.0.1 8007 'hello world'")
    exit()

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print_useage()

    ip = sys.argv[1]
    port = int(sys.argv[2])
    msg = sys.argv[3]

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("Socket creation failed with error.")
        print(err)

    # connect to the echo server
    s.connect((ip, port))

    # pass message to the server
    print("Sending message: ", msg)

	# HTTP requests must end with literal CR + LF  
	#s.send(b'GET /index.html\r\n')
    s.send(msg.encode());

    echo = s.recv(len(msg))
    print(echo.decode())
    s.close()

