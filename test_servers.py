# -*- coding: utf-8 -*-
"""Testing for echo servers."""

from __future__ import unicode_literals
import pytest

ECHO_TABLE = [('zach', 'HTTP/1.1 200 OK\rDate Tue, 24 Oct 2017 21:58:06 GMT\r')]


@pytest.mark.parametrize('n, result', ECHO_TABLE)
def test_client_server(n, result):
    """."""
    from client import client
    from server import response_ok
    assert client(n) == response_ok()


def test_response_ok_is_byte_string():
    """."""
    from server import response_ok
    output = response_ok()
    assert isinstance(output, str)


def test_response_error_is_byte_string():
    """."""
    from server import response_error
    output = response_error()
    assert isinstance(output, str)
