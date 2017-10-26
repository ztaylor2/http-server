# -*- coding: utf-8 -*-
"""Testing for echo servers."""

from __future__ import unicode_literals
import pytest

ECHO_TABLE = ['GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>',
              'GET /zach/is/cool.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>',
              'GET /path/to/something.html HTTP/1.1<CRLF>Host: www.anothersite.com:80<CRLF><CRLF>']

PARSE_TABLE = [('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/path/to/index.html'),
               ('GET /zach/is/cool.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>', '/zach/is/cool.html')]

PARSE_FAIL_TABLE = [('/path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.0<CRLF>Host: www.mysite1.com:80<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF><CRLF>'),
                    ('GET /path/to/index.html HTTP/1.1<CRLF>Host: www.mysite1.com:80<CRLF>')]

URI_RESOLVE_DIR = [('/path/to/', "HTTP/1.1 200 OK\nContent-Type: Directory\n<CRLF>\n/path/to/"),
                   ('/path/to/dir', "HTTP/1.1 200 OK\nContent-Type: Directory\n<CRLF>\n/path/to/dir"),
                   ('/path/to/another/dir', "HTTP/1.1 200 OK\nContent-Type: Directory\n<CRLF>\n/path/to/another/dir")]

URI_RESOLVE_FILE = [('/path/to/file.txt', "HTTP/1.1 200 OK\nContent-Type: txt\n<CRLF>\n"),
                    ('/path/to/file.py', "HTTP/1.1 200 OK\nContent-Type: py\n<CRLF>\n"),
                    ('/path/to/another/file.html', "HTTP/1.1 200 OK\nContent-Type: html\n<CRLF>\n")]

@pytest.mark.parametrize('n', ECHO_TABLE)
def test_client_server(n):
    """Test if valid http request returns ok response."""
    from client import client
    from server import response_ok
    assert client(n) == response_ok()


def test_response_error_is_byte_string():
    """Test invalid http request returns response error."""
    from client import client
    from server import response_error
    assert client('not an http request') == response_error('400', 'Bad Request')


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


@pytest.mark.parametrize('n, result', URI_RESOLVE_DIR)
def test_resolve_uri_directory_condition(n, result):
    """Tests directory condition of resolve uri method."""
    from server import resolve_uri
    assert resolve_uri(n) == result


@pytest.mark.parametrize('n, result', URI_RESOLVE_FILE)
def test_resolve_uri_directory_condition(n, result):
    """Tests directory condition of resolve uri method."""
    from server import resolve_uri
    from server import response_error
    assert resolve_uri(n) == response_error('404', 'Not Found')


def test_returns_file_body_if_request_existing_file():
    from server import resolve_uri
    n = 'test.txt'
    assert resolve_uri(n) == "HTTP/1.1 200 OK\nContent-Type: ini\n<CRLF>\ntest"
