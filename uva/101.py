import sys

n = int(input())
loc = [(x, 0) for x in range(n)]
stack = [[x] for x in range(n)]


def take(a):
    s, i = loc[a]
    stack[s].pop(i)


def take_here_up(s, i):
    t = stack[s][i:]
    stack[s] = stack[s][:i]
    return t


def put(a, s):
    stack[s].append(a)
    loc[a] = (s, len(stack[s]) - 1)


def move_back_all_blocks_on_top_of(a):
    s, i = loc[a]
    for t in take_here_up(s, i + 1):
        put(t, t)


def move_onto(a, b):
    if loc[a][0] == loc[b][0]:
        return
    move_back_all_blocks_on_top_of(a)
    move_back_all_blocks_on_top_of(b)
    take(a)
    put(a, loc[b][0])


def move_over(a, b):
    if loc[a][0] == loc[b][0]:
        return
    move_back_all_blocks_on_top_of(a)
    take(a)
    put(a, loc[b][0])


def pile_onto(a, b):
    if loc[a][0] == loc[b][0]:
        return
    move_back_all_blocks_on_top_of(b)
    s, i = loc[a]
    for t in take_here_up(s, i):
        put(t, loc[b][0])


def pile_over(a, b):
    if loc[a][0] == loc[b][0]:
        return
    s, i = loc[a]
    for t in take_here_up(s, i):
        put(t, loc[b][0])


def print_state():
    for i in range(n):
        if stack[i]:
            print('%s: %s' % (i, ' '.join([str(x) for x in stack[i]])))
        else:
            print('%s:' % i)


for line in sys.stdin:
    c = line.split()
    if len(c) == 1 and c[0] == 'quit':
        print_state()
        break
    else:
        locals()[c[0] + '_' + c[2]](int(c[1]), int(c[3]))

