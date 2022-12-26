from collections import deque
class Graphy:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        # adjList = [[],[],[]...n*]
        for (head, leaf) in edges:
            # dedges = [(head, leaf),(head, leaf),...]
            self.adjList[head].append(leaf)
            # adjList = [[head, leaf], [head, leaf],...]
            self.adjList[leaf].append(head)
            # adjList = [[head, leaf], [head, leaf], [leaf, head], [leaf, head]...]

def bfs(graphy, vertex, discovered):
    q = deque()
    # q = [] with special functions -- that is deque
    
    discovered[vertex] = True
    # discovered = [False, False, False, True, False, ...]
    q.append(vertex)
    
    while q:
        vertex = q.popleft()
        print(vertex, end = " ")
        
        for u in graphy.adjList[vertex]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)

if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)]
    n = 15
    graphy = Graphy(edges, n)
    
    discovered = [False] * n
    print(discovered)
    for i in range(n):
        if not discovered[i]:
            bfs(graphy, i, discovered)