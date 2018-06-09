# This is to calculate the minimum crossing edge between two groups of data, not necessaril
# two min cuts because the two partition might not be applicable in reality.

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
        for j in range(1, len(a[u_list[i]-1])):
            if FindAInB(a[u_list[i]-1][j],v_list) == 1:
                crossing_edge += 1
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
            A.append([int(x) for x in line.strip().split()])
    mincut = FindMinCut(A, N, M)
    print(mincut)

main()