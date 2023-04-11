from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Device 1 is connected by', addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == 'Request':
            temperature = str(random.randint(0, 40))
            humidity = str(random.randint(0, 100))
            illuminance = str(random.randint(70, 150))

            conn.sendall(f'Device 1: Temp={temperature}, Humid={humidity}, Illum={illuminance}'.encode())
        elif data == 'quit':
            print('quit')
            conn.close()
            #s.close()
            break
    
    conn.close()