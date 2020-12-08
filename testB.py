def bfspath2(graph, source, sink):
    queue = [[source]]
    visited = []
    path_found = False

    while queue:
        
        path = queue.pop(0)
        node = path[-1]        
        if node == sink:
            path_found = True
            return path, True

        if node not in visited:
            for adjacent in graph.get(node, []):
                
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.append(node)
    return [], False


def getminWeight(path, dictionary):
    weights = []
    for i in range(len(path)-1):
        weights.append(dictionary.get((path[i], path[i+1])))
        
    print(max(weights)) 





class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []    
     
    def addEdge(self, a, b, weight):
        self.graph.append([a, b, weight])
 
    def find(self, p, i):
        if p[i] == i:
            return i
            # finds the parent recursively
        return self.find(p, p[i])
 
    # applies union find
    def union(self, p, rank, x, y):
        # r1 r2 are the roots
        r1 = self.find(p, x)
        r2 = self.find(p, y)
 
        if rank[r1] < rank[r2]:
            p[r1] = r2
        elif rank[r1] > rank[r2]:
            p[r2] = r1
        else:
            p[r2] = r1
            rank[r1] += 1
 
    def kruskal(self):
        MST = dict((i, []) for i in range(n)) # the graph form of the MST
        nonweightedMST = dict((i, []) for i in range(n))
 
        i = 0
        edge_number = 0
 
        self.graph =  sorted(self.graph, key=lambda item: item[2])
 
        parent, rank = [], []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        while edge_number < self.V-1:	
            u, v, w =  self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # if they don't share same parent
            if x != y:
                edge_number += 1  
                # making the graph
                MST[u].append((v,w))
                MST[v].append((u,w))
                nonweightedMST[u].append(v)
                nonweightedMST[v].append(u)
                # apply union to tree => updates graph
                self.union(parent, rank, x, y) 

        return MST, nonweightedMST


first_line = list(map(int, input().split()))

n, m = first_line[0], first_line[1]

graph = Graph(n)

edge_weight = {}
for k in range(m):
    line = list(map(int, input().split()))
    #print("Line :", line)
    graph.addEdge(line[0]-1, line[1]-1, line[2])
    
    # setting edge - weight map
    edge_weight[line[0]-1, line[1]-1] = line[2]
    edge_weight[line[1]-1, line[0]-1] = line[2]

MinSpanT, nonweightedMST = graph.kruskal()
#print(bfspath2(nonweightedMST, 0, n-1))
getminWeight(bfspath2(nonweightedMST, 0, n-1)[0], edge_weight)
# we'll use this to compute a path from the source to the sin within the MST



# from the kruskal graph, we can find a path from source to sink 
"""
python3 /Users/kawa/Desktop/EPFL/BA3/Algorithms/"implementati0on 2"/testB.py < /Users/kawa/Desktop/EPFL/BA3/Algorithms/"implementati0on 2"/testsB/16.txt
"""