import random

flag = [0]*700

with open("flag.txt","rb") as f:
    hidden = f.read()
    for _ in range(len(hidden)):
        flag[_] = hidden[_]

for _ in range(700):
    print(random.getrandbits(32)+flag[_])
    input()