import socket
import time
import threading

clients = []
server_addr = ('', 2500)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(server_addr)
s.listen(5)

print('Server Started')

# 클라이언트 처리 스레드
def client_thread(conn, addr):
    # 새로운 클라이언트이면 목록에 추가
    if (conn, addr) not in clients:
        print('new client', addr)
        clients.append((conn, addr))

    while True:
        data = conn.recv(1024)
        if not data:
            break
        # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if 'quit' in data.decode():
            if (conn, addr) in clients:
                print(addr, 'exited')
                clients.remove((conn, addr))
                continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        # 모든 클라이언트에게 전송
        for client in clients:
            if client[1] != addr:
                client[0].send(data)

    conn.close()

while True:
    conn, addr = s.accept()
    threading.Thread(target=client_thread, args=(conn, addr)).start()