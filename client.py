# -*- coding: utf-8 -*-
"""Creates a client to communicate with a server."""
from __future__ import unicode_literals

import sys
import socket


def client(message):
    """Instantiate a client and routes the clients message to a server."""
    infos = socket.getaddrinfo('127.0.0.1', 9001)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message += '|~|'
    client.sendall(message.encode('utf8'))

    message = ""

    buffer_length = 8
    reply_complete = False
    while not reply_complete:
        part_recv_message = client.recv(buffer_length)
        message += part_recv_message.decode('utf8')
        if len(part_recv_message) < buffer_length:
            break
        elif message.endswith('|~|'):
            print(True)
            break
    client.close()
    return message[:]


if __name__ == '__main__':
    print(client(sys.argv[1]))
