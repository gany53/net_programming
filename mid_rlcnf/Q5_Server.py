#udp에는 connect가 없음 tcp에는 있음, tcp는 bind 후 listen, 

import socket

#소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#소켓 바인드
sock.bind(('', 9000))
#연결 대기
sock.listen(2)

# 메시지를 저장할 딕셔너리
messages = {}

#클라이언트와 연결이 수립되면 처리
client, addr = sock.accept()
print('Connection from ', addr)

while True:
    # 클라이언트로부터 메시지 수신
    data = client.recv(1024).decode()
    if not data:
        break
    # 'send [mboxID] message' 형식인 경우
    if data.startswith('send '):
        try:
            mbox_id, message = data.split(' ', 2)[1:]
            messages.setdefault(mbox_id, []).append(message)
            client.sendall('OK'.encode())
        except:
            client.sendall('Invalid message format'.encode())
    # 'receive [mboxID]' 형식인 경우
    elif data.startswith('receive '):
        try:
            mbox_id = data.split(' ')[1]
            if mbox_id in messages and len(messages[mbox_id]) > 0:
                message = messages[mbox_id].pop(0)
                client.sendall(message.encode())
            else:
                client.sendall('No messages'.encode())
        except:
            client.sendall('Invalid message format'.encode())
    # 'quit' 형식인 경우
    elif data == 'quit':
        client.sendall('bye'.encode())
        break
    else:
        client.sendall('Invalid message format'.encode())

# 소켓 종료
client.close()
sock.close()


# UDP
# import socket

# # UDP 소켓 생성
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(('localhost', 9000))

# # 메시지를 저장할 딕셔너리 생성
# messages = {}

# while True:
#     # 클라이언트로부터 메시지 수신
#     data, addr = sock.recvfrom(1024)
#     message = data.decode()
    
#     # 'send [mboxID] message' 메시지 처리
#     if message.startswith('send '):
#         _, mboxID, msg = message.split(' ', 2)
#         if mboxID in messages:
#             messages[mboxID].append(msg)
#         else:
#             messages[mboxID] = [msg]
#         # 'OK' 메시지 전송
#         sock.sendto('OK'.encode(), addr)
        
#     # 'receive [mboxID]' 메시지 처리
#     elif message.startswith('receive '):
#         _, mboxID = message.split()
#         if mboxID in messages and messages[mboxID]:
#             # 메시지 전송 후 삭제
#             msg = messages[mboxID].pop(0)
#             sock.sendto(msg.encode(), addr)
#         else:
#             # 해당 mboxID의 메시지가 없는 경우 'No messages' 메시지 전송
#             sock.sendto('No messages'.encode(), addr)
            
#     # 'quit' 메시지 처리
#     elif message == 'quit':
#         break

# # 소켓 닫기
# sock.close()