from socket import *
import os

def split(req):
    filename = req[0].split(' ')[1][1:]
    return filename

def open(filename, mimeType, c, f):
    if os.path.isfile(filename):
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(('Content-Type: ' + mimeType + '\r\n').encode())
        c.send(b'\r\n')

        data = f.read()
        if filename == 'index.html':
            c.send(data.encode('euc-kr'))
        else:
            c.send(data)
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    
s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    filename = split(req)
    
    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'

    open(filename, mimeType, c, f)

    c.close()