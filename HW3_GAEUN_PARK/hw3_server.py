import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connetion from ', addr)

    client.send(b'Hello ' + addr[0].encode())

    stuName = client.recv(1024)
    print(stuName.decode())
    
    stuId = 20201500
    stuId = stuId.to_bytes(4,'big')
    client.send(stuId)

    client.close()