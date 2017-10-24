"""."""

import sys
import socket


def server():
    """."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5555)
    server.bind(address)
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

    print(message)

    conn.close()


if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        # close all open sockets
        print("\nGoodbye")
        sys.exit()
