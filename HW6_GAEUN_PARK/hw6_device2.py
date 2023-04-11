from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Device 2 is connected by', addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == 'Request':
            heartbeat = str(random.randint(40, 140))
            steps = str(random.randint(2000, 6000))
            calorie_burn = str(random.randint(1000, 4000))

            conn.sendall(f'Device 2: Heartbeat={heartbeat}, Steps={steps}, Cal={calorie_burn}'.encode())
        elif data == 'quit':
            print('quit')
            conn.close()
            #s.close()
            break

    conn.close()