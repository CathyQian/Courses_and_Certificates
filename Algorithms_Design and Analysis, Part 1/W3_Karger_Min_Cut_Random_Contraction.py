import copy
import random

def FindAInB(a, b):  # check whether element a is in list b; if return 1
    flag = 0
    for j in range(1, len(b)):
        if  a == b[j]:
            flag = 1
            break
    return flag

def merge2( a ):
    vertex2index = {v : idx for idx, v in enumerate( x[ 0 ] for x in a )}
    
    u_list = random.choice( a )
    u = u_list[ 0 ]
    v = random.choice( u_list[ 1: ] )
    print( 'u,v', u, v )
    v_list = a[ vertex2index[ v ] ]    
    
    new_u = [ u ]
    new_u.extend( i for i in u_list[ 1: ] if i != v )
    new_u.extend( i for i in v_list[ 1: ] if i != u )
    
    a[ vertex2index[ u ] ] = new_u
    a.pop( vertex2index[ v ] )
    
    for i in range( len( a ) ):
        x = a[ i ]
        if x[ 0 ] == u:
            continue
        new_x = [ x[ 0 ] ]
        
        for j in x[ 1: ]:
            if j != v:
                new_x.append( j )
            else:
                new_x.append( u )
                
        a[ i ] = new_x
        
    return a, len( a )
    
    

def MergeTwoRandomVertices(a, N): 
    vertices = [] # store all vertices index
    for i in range(N):
       # print('N,i', N, i)
        vertices.append(a[i][0])
        #print(i, vertices)
    vertex2index = {v : idx for idx, v in enumerate(vertices)}
    u = random.choice(vertices) #randomly pick two vertices
    u_ind = vertex2index[u]
    v = random.choice(a[u_ind][1:])
    v_ind = vertex2index[v]
    u_new = [ u ]
    for i in range(1, len(a[u_ind])):
        if a[u_ind][i] != v:
            u_new.append(a[u_ind][i])
    for j in range(1, len(a[v_ind])):
        if a[v_ind][j] != u: 
            u_new.append(a[v_ind][j])
    a[u_ind] = u_new
    a.remove(a[v_ind])
    N = N - 1
    i = 0
    while i < N:
        new_list = []
        for j in range(len(a[i])):
            if a[i][j] != v:
                new_list.append(a[i][j])
            else:
                new_list.append(u)
        a[i] = new_list 
        i += 1               
    
    # print(u, v)
    return a, N
    
def RandomContraction (a, N):
    cut = 0
    while N > 2:
        (a, N) = MergeTwoRandomVertices(a, N)
#        a, N = merge2( a )
    if N == 2: # when there is only 2 vertices
        cut = len(a[0])-1
#        print ('a0', a[0])
#        print ('a1', a[1])
    #print('This is cut and N in RandomContraction:\n', cut, N)
    return cut
    #merge two random vertices, update a and N
def FindMinCut(a, N, M):
    cut = []
    b = copy.deepcopy(a)
    n = N
    for j in range(M):
        a = copy.deepcopy(b)
        N = n
        cut.append(RandomContraction(a, N))     
#    print('This is cut in FindMinCut:\n', cut)
    return min(cut)

def main():
    N = 200
    M = N
    A = []
    with open("W3_kargerMinCut.txt", "r") as ins:
        for line in ins:
            A.append([int(x) for x in line.strip().split()])
    mincut = FindMinCut(A, N, M)
    print(mincut)

main()

