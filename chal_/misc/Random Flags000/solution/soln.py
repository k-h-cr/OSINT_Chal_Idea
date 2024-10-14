from extend_mt19937_predictor import ExtendMT19937Predictor
import socket

nc_server = ['placeholder.server', 1234]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(nc_server[0],nc_server[1])

values = []
for _ in range(700):
    values.append(int(sock.recv(1024).decode()))
    sock.send("\n".encode())

predictor = ExtendMT19937Predictor()

for i in range(624,0,-1):
    predictor.setrandbits(values[-i], 32)

backtrack = [predictor.backtrack_getrandbits(32) for _ in range(700)][::-1]
for _ in range(700):
    print(chr(values[_] - backtrack[_]),end="")
