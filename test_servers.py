# -*- coding: utf-8 -*-
"""Testing for echo servers."""

from __future__ import unicode_literals
import pytest


PARSE_TABLE = [('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/path/to/index.html'),
               ('GET /zach/is/cool.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/zach/is/cool.html')]

PARSE_FAIL_TABLE = [('/path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.0<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF>')]


def test_bad_request_error():
    """Test invalid http request returns response error."""
    from client import client
    from server import response_error
    assert client('not an http request') == response_error('400', 'Bad Request')


def test_not_found_error():
    """Test invalid http request returns response error."""
    from client import client
    from server import response_error
    assert client('GET not_a_webpage.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>') == response_error('404', 'Not Found')


@pytest.mark.parametrize('n, result', PARSE_TABLE)
def test_parse_request(n, result):
    """Test if proper http request parse correctly."""
    from server import parse_request
    parse_request(n) == result


@pytest.mark.parametrize('n', PARSE_FAIL_TABLE)
def test_parse_error_request(n):
    """Test if impropper http request parse send error."""
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request(n)


def test_resolve_uri():
    """Test if resolve uri returns correct vals."""
    from server import resolve_uri
    resolve_uri('test.txt') == (b'txt', b'content of test file', b'20')
