def Swap(A, i, j):
 temp = A[i]
 A[i] = A[j]
 A[j] = temp

def BubbleSort(A):
    for i in range(len(A)-1) :
        for j in range(len(A)-i-1) :
            if A[j+1] < A[j] :
                Swap(A, j+1, j)

A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]


BubbleSort(A4)
print(A4)
BubbleSort(A5)
print(A5)
BubbleSort(A6)
print(A6)