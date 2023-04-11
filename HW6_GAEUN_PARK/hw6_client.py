from socket import *
import time

while True:
    device = input("Enter device number (1 or 2) or type 'quit': ")

    s = socket(AF_INET, SOCK_STREAM)

    #디바이스 1
    if device == '1':
        s.connect(('localhost', 9000))
        s.sendall('Request'.encode())
        data = s.recv(1024).decode()
        current_time = time.strftime('%a %b %d %H:%M:%S %Y')
        data_with_time = f"{current_time}: {data}"
        print(data_with_time)

        with open('data.txt', 'a') as f:
            f.write(f"{data_with_time}\n")

    #디바이스 2
    elif device == '2':
        s.connect(('localhost', 7777))
        s.sendall('Request'.encode())
        data = s.recv(1024).decode()
        current_time = time.strftime('%a %b %d %H:%M:%S %Y')
        data_with_time = f"{current_time}: {data}"
        print(data_with_time)

        with open('data.txt', 'a') as f:
            f.write(f"{data_with_time}\n")

    if device == 'quit':
        print('quit')
        dev1 = 9000
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', dev1))
        s.sendall('quit'.encode())
        s.close()
        dev2 = 7777
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', dev2))
        s.sendall('quit'.encode())
        s.close()
        break

    else:
        print("Invalid input. Please enter '1', '2', or 'quit'.")
        continue
    
s.close()