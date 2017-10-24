"""."""

import sys
import socket


def client(message):
    """."""
    # open socket connection to server
    # send message var to server through socket
    # accumulate any reply into a string
    # once full reply is recieved close socket and return the mesasge
    infos = socket.getaddrinfo('127.0.0.1', 5555)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    print(client)
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))

    client.close()


if __name__ == '__main__':
    client(sys.argv[1])
