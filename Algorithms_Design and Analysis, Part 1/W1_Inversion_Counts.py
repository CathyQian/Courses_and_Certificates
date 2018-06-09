
def SortAndCount(A, n):
    print('Sort A=', A)
    if n == 1:
        return (A, 0)
    else:
        h = n//2
        A_l = A[:h]
        A_r = A[h:]
        (B, x) = SortAndCount(A_l, len(A_l))
        (C, y) = SortAndCount(A_r, len(A_r))
        (D, z) = MergeAndCountSplitInv(B, C, len(B+C))  ## update B and C here
        print('D in SortAndCount', D)
        return (D, x+y+z)
        
        
def MergeAndCountSplitInv(A_l, A_r, n):
    i = 0
    j = 0
    m = 0
    D = []
    h = len(A_l) 
    while i < h and j < n-h: # use while loop instead of for loop
            if A_l[i] <= A_r[j]:
                D.append(A_l[i])
                i = i + 1                
                break
            elif A_r[j] < A_l[i]:
                D.append(A_r[j])
                m = m + h - i
                j = j + 1
    if i < h: # better than if len(D) < n and i < h
        for x in range(i , h):
            D.append(A_l[x])
    elif j < n-h:
        for x in range(j, n - h):
            D.append(A_r[x])
    return (D, m)
    
def main():
    
    A = [ 6, 5, 4, 3, 2, 1]
#    A = [int(line) for line in open('W1_homework_IntegerArray.txt')]
    D = []
    (D, m) = SortAndCount(A, len(A))
    print (D, m)
    
main()

#integers = []
#infile = open( 'SJDFKDJFL' )
#for line in infile:
#    integers.append(int(line))
    
#myList = []
#for i in range(n):
#    myList.append(0)
#    
#myList = [0 for i in range(n)]