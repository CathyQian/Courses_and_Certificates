""" Dijkstra's algorithm to find the shortest path in undirected graph, from 
node 1 to any other nodes. Output shortest path length"""



"""read each line into graph_dict. For any even i, value[i] is node and 
value [i+1] is distance between key and value[i]"""

def ReadIntoDict(graph):
    with open("W5_dijkstraData.txt", "r") as ins:
        for line in ins:
            line = line.replace(',',' ')
            temp = [int(x) for x in line.strip().split()]
            graph[temp[0]] = temp[ 1: ]
#            temp.remove(temp[0])
    return graph


"""calculate shortest distance
if no shortest path between 1 and s, we define dist as 1000000"""
 
"""O(mn) time, each edge scanned multiple times"""       
def DijkstraShortestPath(graph, VertX):
    graphcopy = graph.copy() 
    VertX[1] = 0
    print(VertX)
    del graph[1]
    while len(graph) > 0:
        X = []
        for key in VertX.keys():
            X.append(key)
        minvalue = 10**6
        for i in range(len(X)):
            linkednodes = graphcopy[X[i]]
            for j in range(len(linkednodes)//2):
                if linkednodes[2*j] in graph.keys() and VertX[X[i]] + linkednodes[2*j+1] < minvalue:
                    minvalue = VertX[X[i]] + linkednodes[2*j+1]
                    minnodeG = linkednodes[2*j]
        if minvalue != 10**6:# if can find any edges between X and graph (= V-X)
            VertX[minnodeG] = minvalue
            del graph[minnodeG]
            
        else:
            for k in graph.keys():
                VertX[k] = 10**6
            graph = {}
    return VertX
        
        
"record shortest path every time, faster"        
def DijkstraShortestPath2(graph, VertX):
    Q = {}
    INFINITY = 10**6
    for key in graph.keys(): #initialiazation
        Q[key] = INFINITY 
    Q[1] = 0
    while len(Q) > 0:
        for key in Q.keys():
            if Q[key] == min(Q.values()):
                u = key        
        linkednodes = graph[u]
        print('This is linkednodes:', linkednodes)
        for j in range(len(linkednodes)//2):
            print('This is j:', j)
            print(linkednodes[2*j]) 
            print('This is Q.keys()', Q.keys())
            print(Q[u] + linkednodes[2*j+1])
            if linkednodes[2*j] in Q.keys() and (Q[u] + linkednodes[2*j+1]) < Q[linkednodes[2*j]]:
                Q[linkednodes[2*j]] = Q[u] + linkednodes[2*j+1]  
        VertX[u] = Q[u]
        del Q[u]               
    return VertX



        
def main():
    graph = {}
    VertX = {}
    graph = ReadIntoDict(graph)
    VertX = DijkstraShortestPath2(graph, VertX)
    print('This is VertX:', VertX)
    nodes = [7,37,59,82,99,115,133,165,188,197]
    dist = []
    for i in range(len(nodes)):
        dist.append(VertX[nodes[i]])
    print('This is shortest dist:', dist)
    
#graph = {1:'a', 3:'b', 2:'c'}
#VertX = {}
#for k in graph.keys():
#    VertX[k] = 10**6
#print(VertX)

main()
