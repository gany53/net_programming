#tcp는 listen - connect - accept
#tcp는 client에 connect가 있어야 하고, server에 listen과 accept가 있어야 함
#sendall은 TCP, 처음은 send 써보고 안되면 sendall
#sendto는 UDP

import socket

HOST = 'localhost'  # 서버 호스트 이름
PORT = 8888  # 서버 포트 번호

# 서버에 연결
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

while True:
    # 사용자로부터 메시지 입력
    msg = input('Enter your message: ')
    # 서버로 메시지 전송, sock.sendall()은 TCP에 주요 사용
    sock.sendall(msg.encode())
    # 'quit' 메시지인 경우
    if msg == 'quit':
        break
    # 서버로부터 응답 수신
    data = sock.recv(1024).decode()
    print(data)

# 소켓 종료
sock.close()


# UDP
# import socket

# # UDP 소켓 생성
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     # 사용자로부터 메시지 입력받기
#     message = input('Enter message: ')
    
#     # 메시지 전송
#     sock.sendto(message.encode(), ('localhost', 9000))
    
#     # 'quit' 메시지인 경우 프로그램 종료
#     if message == 'quit':
#         break
    
#     # 응답 수신 및 출력
#     data, addr = sock.recvfrom(1024)
#     print(data.decode())

# # 소켓 닫기
# sock.close()
