# HTTP-Server
An http server built in python.

## HTTP Resources
-------------------
[Stack Overflow - Carriage](https://stackoverflow.com/questions/1761051/difference-between-n-and-r)

[Stack Overflow - Flush](https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method)

[Code Fellows](https://codefellows.github.io/sea-python-401d7/lectures/http.html#wrap-up)

### How to format time in the server
--------------------------------------
```import email.utils

var = 'Date {}'.format(email.utils.formatdate(usegmt=True)).encode('utf8')
```

### How to set a response
---------------------------
```response = "HTTP/1.1 INSERT ERROR"```