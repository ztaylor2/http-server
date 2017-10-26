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


def response_error(error_code, reason_phrase):
    """Function sends a 500 Internal Server Error response."""
    message = "HTTP/1.1 {} {}\r\n".format(error_code, reason_phrase)
    message += 'Date {}\r\n'.format(email.utils.formatdate(usegmt=True))
    return message


def parse_request(req):
    """Recieve a request from the client and parses it."""
    try:
        first_line_req = req.split("<CRLF>")[0].split(" ")
        sec_line_req = req.split("<CRLF>")[1].split(" ")
    except IndexError:
        raise ValueError("Invalid request")

    if first_line_req[0] != "GET":
        raise ValueError("Invalid HTTP Method - GET method required")

    if first_line_req[2] != "HTTP/1.1":
        raise ValueError("Invalid HTTP Type - HTTP/1.1 is required")

    if sec_line_req[0] != "Host:":
        raise ValueError("Invalid Host")

    if req[-12:] != "<CRLF><CRLF>":
        raise ValueError("Response not properly closed - Requires two carriages at the end")

    return first_line_req[1]


def server():
    """Create a server that echos messages with client."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 9000)
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
            message = str(message[:-3])
            try:
                sys.stdout.write(parse_request(message))
                conn.sendall(response_ok().encode('utf8'))
                # sys.stdout.write(response_ok())
            except ValueError:
                conn.sendall(response_error('400', 'Bad Request').encode('utf8'))
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nGoodbye")
        conn.close()
        server.close()
        sys.exit()

if __name__ == '__main__':
    print('Server Running\n')
    server()
