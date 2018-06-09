"""compute strongly connected components
key point:
1) use dictionary to store adjacency list, so that it is easy to see which nodes are connected
2) reverse graph (store data in dictionary makes it easy)
3) use one class to check status of all nodes sharing similar parameters

"""

import sys
#import time
#import resource
from itertools import groupby
from collections import defaultdict
 
 
#set rescursion limit and stack size limit
sys.setrecursionlimit(10000)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
 
 
class Track(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes."""
 
    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()
 
 
def dfs(graph_dict, node, track):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail node: [head nodes]}. Depth first search runs recrusively and keeps
    track of the parameters"""
#    print("dfs", node)
    track.explored.add(node)
    track.leader[node] = track.current_source
    for head in graph_dict[node]:
        if head not in track.explored:
            dfs(graph_dict, head, track)
    track.current_time += 1
    track.finish_time[node] = track.current_time
 
 
def dfs_loop(graph_dict, nodes, track):
    """Outter loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""
 
    for node in nodes:
        if node not in track.explored:
            track.current_source = node
            dfs(graph_dict, node, track)
 
 
def scc(graph, reverse_graph, nodes):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on orignial graph with nodes in decreasing finish
    time order(obatined from firt run). Return a dict of {leader: SCC}."""
    
    out = defaultdict(list)
    track = Track()
    dfs_loop(reverse_graph, nodes, track)
    sorted_nodes = sorted(track.finish_time,
                          key=track.finish_time.get, reverse=True)
    track.current_time = 0
    track.current_source = None
    track.explored = set()
    dfs_loop(graph, sorted_nodes, track)
    for lead, vertex in groupby(sorted(track.leader, key=track.leader.get),
                                key=track.leader.get):
        out[lead] = list(vertex)
    return out
    




def main_graph_dict():
    graph_dict = {} 
    seen = set()
#    with open("W4_SCC_test.txt", "r") as ins:
    with open("W4_StronglyConnectedComponents.txt", "r") as ins:
        for line in ins:
            temp = []
            temp = [int(x) for x in line.strip().split()]
            if temp[0] not in graph_dict:
                value = []
                graph_dict[temp[0]] = value
                value.append(temp[1])
                seen.add(temp[1])
            else:
                value = graph_dict[temp[0]]
                value.append(temp[1])
                seen.add(temp[1])

    # Check to see all nodes we've seen have an entry in the
    # graph dictionary. If not, add a self-loop to fill it in.
    for node in seen:
        if node not in graph_dict:
            graph_dict[node] = [node]

#    print("GRAPH", graph_dict)
    return graph_dict


def ReverseGraphDict(graph_dict):
    reverse_graph_dict = {}
    graph_keys = list(graph_dict.keys())
    for i in range(len(graph_keys)):
        old_value = graph_dict[graph_keys[i]]#if graph_keys[i] not in reverse_graph_dict.values():
        for j in range(len(old_value)):
            if old_value[j] not in reverse_graph_dict:# value [j] is not a key
                reverse_graph_dict[old_value[j]] = [graph_keys[i]]
                
            else:
                new_value = reverse_graph_dict[old_value[j]]
                new_value.append(graph_keys[i])
                
    # Finally check for presence of all nodes in reverse_graph.
    # If any nodes are missing in reverse_graph, they need to be
    # added as self-loops.
    for node in graph_keys:
        if node not in reverse_graph_dict:
            reverse_graph_dict[node] = [node]
                
#    print("REVERSE",reverse_graph_dict)
    return reverse_graph_dict           

def main():
    graph_dict = main_graph_dict()
    #print("read graph")
    reverse_graph_dict = ReverseGraphDict(graph_dict)
    #print("constructed reverse graph")
    nodes = list(graph_dict.keys())
    #print("computing scc")
    result = scc(graph_dict, reverse_graph_dict, nodes)
    print("result", sorted(list(len(value) for value in result.values()), reverse=True))
    
main()

