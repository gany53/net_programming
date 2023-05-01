from socket import *
from time import sleep

BUFF_SIZE = 1024
port = 5555
c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))

for i in range(10): # 10번 전송
    count = 0
    time = 0.1 # 0.1초
    data = 'Hello, IoT'
    while True:
        c_sock.send(data.encode()) #ack 전송
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)
        try:
            data = c_sock.recv(BUFF_SIZE)
        except timeout:
            if count == 3:
                break
            count += 1
            sleep(1)
        else:
            print('Response', data.decode())
            break