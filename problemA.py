first_line = list(map(int, input().split()))

n, m = first_line[0], first_line[1]

# basically shows the residual graph
adj_list = dict((i, []) for i in range(1, n+1))
for k in range(m):
    line = list(map(int, input().split()))
    i, j = line[0], line[1]

    adj_list.get(i).append(j)
    if i != 1 and j != n:
        adj_list.get(j).append(i)

# first residual graph
residual = adj_list

# simply finds a path from source to sink
def bfspath(graph, start, end):
    queue = [[start]]
    visited = []
    path_found = False
    #queue.append([start])
    #visited.append(start)

    while queue:
        
        #print("queue before pop :", queue)
        path = queue.pop(0)
        #last_path = path[:-1]
        #print("last path: ", last_path)
        #print("queue after pop  :", queue)
        node = path[-1]
        #print("node visited", node )
        
        if node == end:
            path_found = True
            #print("path :", path)
            #print("queue returned", queue)
            return path, True

        if node not in visited:
            for adjacent in graph.get(node, []):
                
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.append(node)
                #print("hey hey")
    #print("queue ended")
    return [], False

            


#print("adj list", adj_list)

# residual graph is the backwards thing
# if there is a path in residual, update original adj_list & remove the path we found


# re
def augment_path(path, graph, residual):
    # path ist a list []
    # graph ist a dict mapping int -> list
    path_taken = [] # is a list of tuples, to be removed in original graph
    #print(graph)
    for i in range(len(path)-1):
        path_taken.append((path[i], path[i+1]))
    for t in path_taken:
        residual[t[0]].remove(t[1])
        residual[t[1]].append(t[0])
    
    #print("residual",residual)
#remove_path(bfspath(residual, n)[0], resi)



def alg(graph, residual):
    #print("initial residual", residual)
    flow = 0
    pathexists = True
    #queue = [[1]]
    while pathexists:
        path, pathexists = bfspath(residual, 1, n)
        augment_path(path, graph, residual)
        if pathexists:
            flow += 1
        #print(pathexists)
   # print("flow =" , flow)
    #print("done")
    return flow


print(alg(adj_list, residual))




""" test address
python3 /Users/kawa/Desktop/EPFL/BA3/Algorithms/"implementati0on 2"/noqueuesaved.py < /Users/kawa/Desktop/EPFL/BA3/Algorithms/"implementati0on 2"/testsA/16.txt
"""
