# Input: An array A and indices i and j.
# Output: An array where A[i] and A[j] have been swapped.
def Swap(A, i, j):
 temp = A[i]
 A[i] = A[j]
 A[j] = temp
# Input: An array A of integers.
# Output: An array A sorted in increasing order.
def BubbleSort(A):
    # Initializes all counts to zero.
    total_comparisons = 0
    total_swaps = 0
    compared_count = 0
    swap_count = 0
    for i in range(len(A)-1):
        # Creates a flag for when the array is sorted.
        swapped = False
        for j in range(len(A)-i-1):
            if A[j+1] < A[j]:
                Swap(A, j+1, j)
                # Counts each time a swap is made.
                swap_count += 1
                # If a swap is made this will stay true.
                swapped = True
            # Counts each comparison made.
            compared_count += 1
        # Counts the total swaps and comparisons throughout the sorting.
        total_comparisons += compared_count
        total_swaps += swap_count
        print(A)
        print(f"Compared count: {compared_count}")
        print(f"Swapped count: {swap_count}")
        # Resets variables to zero each time through the loop.
        compared_count = 0
        swap_count = 0
        # If there is no swap this will breat out of the loop and the array will be sorted.
        if not swapped:
            break
    print(f"Total compared: {total_comparisons}")
    print(f"Total swapped: {total_swaps}")
    

A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

BubbleSort(A4)
print("\n")

BubbleSort(A5)
print("\n")

BubbleSort(A6)