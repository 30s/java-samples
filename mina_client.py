import time

from socket import *


HOST = '127.0.0.1'
PORT = 9123


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))
    while True:
        print sock.send(''.join('hello\n'))
        time.sleep(1)
        print sock.recv(100)
 
    sock.close()


if __name__ == '__main__':
    main()

