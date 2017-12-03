import sys

r = bytearray()
for c in sys.stdin.buffer.read():
    if c == 10 or c == 13:
        r.append(c)
    else:
        r.append(c - 7)
sys.stdout.buffer.write(r)
