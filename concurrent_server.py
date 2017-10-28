# -*- coding: utf-8 -*-
"""Create a server."""
from __future__ import unicode_literals

import sys
# import socket
import email.utils


def response_ok(file_type, body, len):
    """Function sends a 200 OK response message."""
    message = b"HTTP/1.1 200 OK\r\n"
    message += "Date {}\r\n".format(email.utils.formatdate(usegmt=True)).encode("utf8")
    message += "Content-Length: {}\r\n".format(len).encode("utf8")
    message += "Content-Type: {}\r\n\r\n".format(file_type).encode("utf8")
    message += "{}".format(body).encode("utf8")
    return message


def response_error(error_code, reason_phrase):
    """Function sends a 500 Internal Server Error response."""
    message = "HTTP/1.1 {} {}\r\n".format(error_code, reason_phrase)
    message += "Date {}\r\n".format(email.utils.formatdate(usegmt=True))
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


def resolve_uri(uri):
    """Resolve the URI from http request."""
    if "." not in uri:     # uri is a directory
        # return simple html listing of dir as body of response
        file_type = "Directory"
        body = uri
    else:     # uri is a file, return contents of file as body
        file_type = "{}".format(uri.split(".")[-1])
        with open(uri, "rb") as raw_file:
            body = raw_file.read()
    length = "{}".format(len(body))
    return (file_type, body, length)


def echo(socket, address):
    """Create a server that echos messages with client."""
    try:
        while True:
            message = ""

            buffer_length = 8
            message_complete = False
            while not message_complete:
                part = socket.recv(buffer_length)
                message += part.decode("utf8")
                if len(part) < buffer_length:
                    break
                elif message.endswith("|~|"):
                    break
            message = str(message[:-3])

            try:
                uri = parse_request(message)
            except ValueError:
                socket.sendall(response_error("400", "Bad Request").encode("utf8"))

            try:
                response_ok_http_response = response_ok(*resolve_uri(uri))
                socket.sendall(response_ok_http_response)
            except OSError:
                socket.sendall(response_error("404", "Not Found").encode("utf8"))
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nGoodbye")
        socket.close()
        server.close()
        sys.exit()


if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 10001), echo)
    print('Starting echo server on port 10000')
    server.serve_forever()
