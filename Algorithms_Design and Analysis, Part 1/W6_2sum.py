#
#"""2_sum problem
#Input:unsorted array A of n integers, target sum t
#determine number of t within [-10000, 10000] if there are intergers x and y in A with x+y = t"""
#
#"""1) quick sort A in O(nlogn) time 2) for each x in A, look for t-x in A using dictionary (O(n2logn))"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""Search t-x in A, also make sure that (t-x!=x)"""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def TwoSum(lowbound, highbound, A):
    A_set = set(A)    
    count = 0
    target = lowbound
    for target in range(lowbound, highbound+1):
#        print('target', target)
        for x in A:
            if (target - x) != x and target - x in A_set:
                count = count + 1
                break   
    return count

    

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""main function to calculate number of target value t"""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def main():
    A = []
    with open("W6_prob-2sum.txt", "r") as ins:
        for line in ins:
            A.extend(int(x) for x in line.strip().split())
    print(len(A))
    #A = QuickSort(A, len(A))
    count = 0
    count = TwoSum(-10000, 10000, A)
    print("Number of target values t in the interval [-10000,10000] is:", count)

    
main()