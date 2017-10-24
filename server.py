# -*- coding: utf-8 -*-
"""Create a server."""
from __future__ import unicode_literals

import sys
import socket
import email.utils

def response_ok():
    """Function sends a 200 OK response message"""
    message = b"HTTP/1.1 200 OK \r\n "
    message += u'Date {}\r\n\r\n'.format(email.utils.formatdate(usegmt=True)).encode('utf8')
    return message

def response_error():
    """Function sends a 500 Internal Server Error response"""
    message = b"HTTP/1.1 500 Internal Server Error \r\n "
    message += u'Date {}\r\n\r\n'.format(email.utils.formatdate(usegmt=True)).encode('utf8')
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

            print(message[:-3])
            conn.sendall(message.encode('utf8'))
    except KeyboardInterrupt:
        print("\nGoodbye")
        conn.close()
        server.close()
        sys.exit()

if __name__ == '__main__':
    print('Server Running')
    server()
