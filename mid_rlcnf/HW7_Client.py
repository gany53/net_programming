from socket import *
import random

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('-> ')
    resend = 0

    while resend <= 5:
        resp = str(resend) + ' ' + message
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            resend += 1
            continue
        else:
            break

    if resend > 5:
        sock.sendto(b'fail', ('localhost', port))
        sock.settimeout(None)
        while True:
            try:
                ndata, naddr = sock.recvfrom(BUFFSIZE)
            except timeout:
                break
            if(ndata.decode() == 'nack'):
                print('nack')
                break

    
    sock.settimeout(None)

    while True:
        data, addr = sock.recvfrom(BUFFSIZE) 
        if data.decode() == 'fail':
            sock.sendto(b'nack', ('localhost', port))
            break

        elif random.random() <= 0.5:
            continue
        
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break