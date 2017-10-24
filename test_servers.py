"""Testing for echo servers.

messages shorter than one buffer in length
messages longer than several buffers in length
messages that are an exact multiple of one buffer in length
messages containing non-ascii characters

"""


import pytest

ECHO_TABLE = [('zach', 'zach'),
              ('this message is longer than multiple buffers', 'this message is longer than multiple buffers'),
              ('eightltr', 'eightltr')]


@pytest.mark.parametrize('n, result', ECHO_TABLE)
def test_client_server(n, result):
    """."""
    from client import client
    assert client(n) == result
