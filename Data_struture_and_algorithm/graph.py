import numpy as np
from queue import Queue
# breadth first search
def bfs(v):
    queue = Queue()
    visited = list()
    visited.append(v)
    queue.put(v)
    while not queue.empty():
        vertex = queue.get()
        print(vertex,end=' ')
        for av in adj_list[vertex]:
            if av not in visited:
                visited.append(av)
                queue.put(av)
# depth first search
def dfs(v,visited=None):
    if visited is None:
        visited = set()
    visited.add(v)
    print(v,end=' ')
    for av in adj_list[v]:
        if av not in visited:
            dfs(av,visited)

# adjcent graph using matrix
size_of_matrix = 5
adj_matrix = np.zeros((size_of_matrix,size_of_matrix), dtype=int)
edges = [(0,1),(2,3),(1,4),(1,2),(0,4),(3,4)]

for edge in edges:
    u,v = edge
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1
print('Adjecent Matrix')
for u in adj_matrix:
    for v in u:
        print(v,end=' ')
    print()

# adjacent graph using list

adj_list = dict()
for edge in edges:
    u,v = edge
    if u in adj_list:
        adj_list[u].append(v)
    else:
        adj_list[u] = [v]
    if v in adj_list:
        adj_list[v].append(u)
    else:
        adj_list[v] = [u]
print('\nAdjacent List')
for u,v in adj_list.items():
    print(f'{u} -> {v}')

# bsf traverse
print('\nBFS traverse')
bfs(0)
print('\n\nDFS search')
dfs(0)