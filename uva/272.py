import sys

open_quote = True
for line in sys.stdin.read().splitlines():
    if line:
        r = []
        for c in line:
            if c == '"':
                if open_quote:
                    r.append('``')
                else:
                    r.append("''")
                open_quote = not open_quote
            else:
                r.append(c)
        print(''.join(r))

