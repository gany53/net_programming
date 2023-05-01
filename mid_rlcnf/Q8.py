from socket import *

# rel_s= socket(AF_INET, SOCK_STREAM)
# rel_s.bind(('', 9000))
# rel_s.listen(10)

while True:
    # 릴레이 서버 소켓 생성 및 연결 대기
    rel_s= socket(AF_INET, SOCK_STREAM)
    rel_s.bind(('', 8080))
    rel_s.listen(10)

    # 브라우저로부터 HTTP 요청 메시지 수신
    rel_c, addr = rel_s.accept()
    data = rel_c.recv(1024)
    msg = data.decode()

    # 요청 라인과 host 헤더 추출
    reg = msg.split('\r\n')[0]
    print(reg)
    hostmeg = 'Host: www.daum.net'

    # 외부 서버로 HTTP 요청 메시지 전송
    ext_s = socket(AF_INET, SOCK_STREAM)
    ext_s.connect(('www.daum.net', 80))
    ext_s.send(reg.encode() +b'\r\n'+ hostmeg.encode() +b'\r\n\r\n')

    # 외부 서버로부터 HTTP 응답 메시지 수진 및 릴레이 -> 브라우저
    web_data = ext_s.recv(1024)
    print(web_data.decode())
    rel_c.sendall(web_data)

    # 소켓 종료
    rel_s.close()
    ext_s.close()

# #gpt 코드
# import socket

# HOST = ''  # Symbolic name meaning all available interfaces
# PORT = 8080  # Arbitrary non-privileged port

# def relay_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         s.bind((HOST, PORT))
#         s.listen(1)
#         print(f'Relay server is listening at http://localhost:{PORT}')

#         while True:
#             conn_browser, addr_browser = s.accept()
#             with conn_browser:
#                 print('Connected by', addr_browser)

#                 # Receive request from browser
#                 data = conn_browser.recv(1024)
#                 print('Received from browser:', data)

#                 # Parse the request message from browser
#                 request = data.decode()
#                 request_lines = request.split('\r\n')
#                 request_line = request_lines[0]
#                 url = request_line.split(' ')[1]

#                 # Send request to external server
#                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_server:
#                     s_server.connect(('www.daum.net', 80))
#                     print('Connected to www.daum.net')

#                     # Modify the request message
#                     modified_request = request_line + '\r\n'
#                     modified_request += 'Host: www.daum.net\r\n'
#                     modified_request += '\r\n'

#                     # Send the modified request message to external server
#                     s_server.sendall(modified_request.encode())

#                     # Receive response from external server
#                     response = b''
#                     while True:
#                         data = s_server.recv(1024)
#                         if not data:
#                             break
#                         response += data

#                     # Send the response to browser
#                     conn_browser.sendall(response)

# if __name__ == '__main__':
#     relay_server()