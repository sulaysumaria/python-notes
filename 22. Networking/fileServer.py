import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

print('Server listening on port: ', port)
s.listen(1)

c, addr = s.accept()

fileName = c.recv(1024)

try:
    f = open(fileName, 'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError as e:
    print('File does not exist.')
    print(e)
    c.send(b'File does not exist.')
except Exception as e:
    print(e)

c.close()
