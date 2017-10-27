# -*- coding: utf-8 -*-
"""Testing for echo servers."""

from __future__ import unicode_literals
import pytest

BAD_REQUEST_TABLE = [('not an http request', ('400', 'Bad Request')),
                     ("/path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>", ('400', 'Bad Request')),
                     ("GET /path/to/index.html HTTP/1.0<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>", ('400', 'Bad Request'))]

NOT_FOUND_TABLE = [("GET /not/a/real/file/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>", ('404', 'Not Found')),
                   ("GET /fake/path/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>", ('404', 'Not Found')),
                   ("GET /another/bad/path/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>", ('404', 'Not Found'))]

PARSE_TABLE = [('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/path/to/index.html'),
               ('GET /zach/is/cool.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/zach/is/cool.html')]

PARSE_FAIL_TABLE = [('/path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.0<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF>')]


@pytest.mark.parametrize('n, result', BAD_REQUEST_TABLE)
def test_bad_request_error(n, result):
    """Test invalid http request returns response error."""
    from client import client
    from server import response_error
    assert client(n) == response_error(*result)


@pytest.mark.parametrize('n, result', NOT_FOUND_TABLE)
def test_not_found_error(n, result):
    """Test invalid http request returns response error."""
    from client import client
    from server import response_error
    assert client(n) == response_error(*result)


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
