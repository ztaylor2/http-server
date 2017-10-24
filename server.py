# -*- coding: utf-8 -*-
"""Create a server."""
from __future__ import unicode_literals

import sys
import socket
import email.utils


def response_ok():
    """Function sends a 200 OK response message."""
    message = 'HTTP/1.1 200 OK\r\n'
    message += 'Date {}\r\n'.format(email.utils.formatdate(usegmt=True))
    return message


def response_error():
    """Function sends a 500 Internal Server Error response."""
    message = "HTTP/1.1 500 Internal Server Error\r"
    message += 'Date {}\r'.format(email.utils.formatdate(usegmt=True))
    return message


def server():
    """Create a server that echos messages with client."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5555)
    server.bind(address)
    try:
        while True:
            server.listen(1)
            conn, addr = server.accept()

            message = ""

            buffer_length = 8
            message_complete = False
            while not message_complete:
                part = conn.recv(buffer_length)
                message += part.decode('utf8')
                if len(part) < buffer_length:
                    break
                elif message.endswith('|~|'):
                    print(True)
                    break

            sys.stdout.write(str(message[:-3]))
            sys.stdout.flush()

            conn.sendall(response_ok().encode('utf8'))
    except KeyboardInterrupt:
        print("\nGoodbye")
        conn.close()
        server.close()
        sys.exit()

if __name__ == '__main__':
    print(response_ok())
    print('Server Running')
    server()
