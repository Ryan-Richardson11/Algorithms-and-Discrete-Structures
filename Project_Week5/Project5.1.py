def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def SelectionSort(A):
    compared_count = 0
    swap_count = 0
    # Starts from the end of the list and goes to the beggining, stepping by -1 each time.
    for i in range(len(A)-1, 0, -1):
        m = i

        for j in range(i-1, -1, -1):
            # Checks if A[j] is larger than A[m] instead of smaller.
            if A[j] > A[m]:
                m = j
            compared_count += 1
        Swap(A, i, m)
        swap_count += 1
        print(A)
        print(f"Compared count: {compared_count}")
        print(f"Swapped count: {swap_count}")
        compared_count = 0
        swap_count = 0


A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

SelectionSort(A1)
SelectionSort(A2)
SelectionSort(A3)
