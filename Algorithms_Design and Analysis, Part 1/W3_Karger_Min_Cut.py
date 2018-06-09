""" key point: remember to update both nodes and connections after random 
contraction 
"""

import random

def FindAInB(a, b):  # check whether element a is in list b
    flag = 0
    for j in range(len(b)):
        if  a == b[j]:
            flag = 1
            break
    return flag
            
def RandomContraction (a, N): 
    # randomly partition graph a into two groups 
    u_list = []  
    v_list = []                     # and count the crossing edges between them    
    u_list = random.sample(range(1, N), random.randrange(1, N))
    for j in range(1, N+1):
        if j not in u_list:
            v_list.append(j)
    m = len(u_list)
    crossing_edge = 0
    for i in range(m):
#        print('This is u list: \n', u_list[i])
#        print('This is a[u_list]:\n', a[u_list[i]-1])
        for j in range(1, len(a[u_list[i]-1])):
            if FindAInB(a[u_list[i]-1][j],v_list) == 1:
                crossing_edge += 1
    if crossing_edge == 0:
        print('u = ', u_list)
        print('v = ', v_list)
    return crossing_edge


def FindMinCut(a, N, M):
    cut = []# find min cut in a N is number of list, M is number of iteraterations
    for i in range(M):
        cut.append(RandomContraction(a, N))
    print(cut)
    return min(cut) #find the minimum cut
    
def main():
    N = 200
    M = N*N
    A = []
    with open("W3_kargerMinCut.txt", "r") as ins:
        for line in ins:
            #print('This is line: ', line)
            A.append([int(x) for x in line.strip().split()])
#    print('This is A list input:\n')
#    print(A) # split list and read individual element
    mincut = FindMinCut(A, N, M)
    print(mincut)

main()