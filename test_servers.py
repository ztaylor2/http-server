# -*- coding: utf-8 -*-
"""Testing for echo servers."""

from __future__ import unicode_literals
import pytest

ECHO_TABLE = ['zach', 'another string', 'yet another string']

PARSE_TABLE = [('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/path/to/index.html'),
               ('GET /zach/is/cool.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/zach/is/cool.html')]

PARSE_FAIL_TABLE = [('/path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.0<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF>')]


@pytest.mark.parametrize('n', ECHO_TABLE)
def test_client_server(n):
    """."""
    from client import client
    from server import response_ok
    assert client(n) == response_ok()


def test_response_ok_is_byte_string():
    """."""
    from server import response_ok
    output = response_ok()
    assert output


def test_response_error_is_byte_string():
    """."""
    from server import response_error
    output = response_error()
    assert output


@pytest.mark.parametrize('n, result', PARSE_TABLE)
def test_parse_request(n, result):
    """."""
    from server import parse_request
    parse_request(n) == result


@pytest.mark.parametrize('n', PARSE_FAIL_TABLE)
def test_parse_error_request(n):
    """."""
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request(n)
