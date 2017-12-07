import sys

map = list(range(128))
t = r"`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
for i in range(len(t) - 1):
    map[ord(t[i + 1])] = ord(t[i])

r = ''
for c in sys.stdin.read():
    r += chr(map[ord(c)])
print(r, end='')

