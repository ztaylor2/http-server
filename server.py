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


if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        # close all open sockets
        print("\nGoodbye")
        sys.exit()
