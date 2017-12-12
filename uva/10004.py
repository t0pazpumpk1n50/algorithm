
def dfs(g, u, color, new_color):
    """ -1: not painted, 0: green, 1: red """
    color[u] = new_color
    for v in g[u]:
        if color[v] == new_color:  # a cycle with odd number of vertices on it
            return True
        elif color[v] == -1:
            if dfs(g, v, color, 1-new_color):
                return True
    return False


while True:
    n_vertices = int(input())
    if n_vertices == 0:
        break

    n_edges = int(input())
    g = [[] for _ in range(n_vertices)]
    for _ in range(n_edges):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    color = [-1] * n_vertices
    print('NOT BICOLORABLE.' if dfs(g, 0, color, 0) else 'BICOLORABLE.')

