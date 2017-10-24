# -*- coding: utf-8 -*-
"""Testing for echo servers."""

from __future__ import unicode_literals
import pytest

# ECHO_TABLE = [('zach', 'zach'),
#               ('this message is longer than multiple buffers', 'this message is longer than multiple buffers'),
#               ('eightltr', 'eightltr'),
#               ('non-ascii values å', 'non-ascii values å')]


# @pytest.mark.parametrize('n, result', ECHO_TABLE)
# def test_client_server(n, result):
#     """."""
#     from client import client
#     assert client(n) == result


def test_response_ok_is_byte_string():
    """."""
    from server import response_ok
    output = response_ok()
    assert isinstance(output, bytes)


def test_response_error_is_byte_string():
    """."""
    from server import response_error
    output = response_error()
    assert isinstance(output, bytes)
