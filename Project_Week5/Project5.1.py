# Input: An array A and indices i and j.
# Output: An array where A[i] and A[j] have been swapped.
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
# Input: An array A of integers.
# Output: Array A sorted in increasing order.
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
            # Adds one for each comparison made.
            compared_count += 1
        Swap(A, i, m)
        # Adds one for each swap made.
        swap_count += 1
        print(A)
        print(f"Compared count: {compared_count}")
        print(f"Swapped count: {swap_count}")
        # Resets variables to zero each time through the loop.
        compared_count = 0
        swap_count = 0


A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

SelectionSort(A1)
print("\n")

SelectionSort(A2)
print("\n")

SelectionSort(A3)
