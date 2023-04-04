import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost',9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

#sock.send(b'Gaeun Park')
sock.send('Gaeun Park'.encode())

stuId = sock.recv(1024)
print(int.from_bytes(stuId, 'big'))

sock.close()
