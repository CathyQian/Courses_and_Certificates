"""pay attention to 1) indentation 2) recursion base case 3) recursion starting and ending index of arrays
   A.append and A.extend is slightly different.
"""
def Swap(a, b): #swap a and b
    k = a
    a = b
    b = k
    return a, b
    
#partition array A[l:r] into <p (index l to i-2), p (index i-1), > p (index i to r) three segment
# A[l:r] means from A[l] to A[r-1]; in QuickSort, l=0

# first element as pivot
def Partition1(A, l, r):
    i = l+1
    for j in range(l+1, r): # j = l+1, l+2,.... r-1
        if A[j]<A[l]:#A[l] (first element as pivot)
            if j != i:# swap A[i] and A[j]
                A[i], A[j] = Swap(A[i], A[j])
            i += 1
    A[l], A[i-1] = Swap(A[l], A[i-1])
    return A[l:i-1], A[i-1], A[i:r], i-1
    
# last element as pivot      
def Partition2(A, l, r):
    A[l], A[r-1] = Swap(A[l], A[r-1])
    i = l+1
    for j in range(l+1, r): # j = l+1, l+2,.... r-1
        if A[j]<A[l]:#A[l] (first element as pivot)
            if j != i:# swap A[i] and A[j]
                A[i], A[j] = Swap(A[i], A[j])
            i += 1
    A[l], A[i-1] = Swap(A[l], A[i-1])
    return A[l:i-1], A[i-1], A[i:r], i-1

# Median element as pivot
def Partition3(A, l, r):
    if A[l] < A[r-1] < A[(r-l-1)//2] or A[(r-l-1)//2] < A[r-1] < A[l]:
        A[l], A[r-1] = Swap(A[l], A[r-1])
    elif A[l] < A[(r-l-1)//2] < A[r-1] or A[r-1] < A[(r-l-1)//2] < A[l]:
        A[l], A[(r-l-1)//2] = Swap(A[l], A[(r-l-1)//2])
    else: 
       pass
    i = l+1
    for j in range(l+1, r): # j = l+1, l+2,.... r-1
        if A[j]<A[l]:#A[l] (first element as pivot)
            if j != i:# swap A[i] and A[j]
                A[i], A[j] = Swap(A[i], A[j])
            i += 1
    A[l], A[i-1] = Swap(A[l], A[i-1])
    return A[l:i-1], A[i-1], A[i:r], i-1
    
    
def QuickSort(A, r, comparison):# number of elements = r
    comparison += r-1
#    print('Comparison is: ', comparison)
    Aleft = []
    Aright = []
    if r == 1:#base case, only one element
        pass        
    elif r == 2:#base case, two elements
        if A[0] > A[r-1]:
            A[0], A[r-1] = Swap(A[0], A[r-1])    
    else: # Partition only works for len(A)>=3
        Aleft, p, Aright, h = Partition3(A, 0, r)# h is index of p
        if h > 1:
            Aleft, comparison = QuickSort(Aleft, h, comparison)
            A[0:h] = Aleft# sort left part (<p)
        if r-h > 1:
            Aright, comparison = QuickSort(Aright, r-h-1, comparison)
            A[h+1:r] = Aright
        A[h] = p
#        print(A, comparison)
    return A, comparison
    
def main():
    A = [] # A is list of list
    with open("W2_QuickSort.txt", "r") as ins:
        for line in ins:
            #A.append(int(line))
            A.extend(int(x) for x in line.strip().split())
    comparison = 0
    A, comparison = QuickSort(A, len(A), comparison)
    print('Comparison is:', comparison)
#    print('A is:', A)
    
    
main()

    