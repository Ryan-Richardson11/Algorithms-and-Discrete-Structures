# Input: An array of real numbers
# Output: Returns the smallest gap between two numbers in the given array
def find_smallest_gap(A):
    size_array = len(A)
    # sets gap equal to difference between the first two numbers in the array.
    gap = abs(A[1] - A[0])
    for i in range(size_array-1):
        for j in range(i+1, size_array):
            if abs(A[i]-A[j]) < gap:
                # if the difference is smaller than the previous gap, it becomes the new gap.
                gap = abs(A[i] - A[j])
    return gap

print(find_smallest_gap([50, 120, 250, 100, 20, 300, 200]))
print(find_smallest_gap([12.4, 45.9, 8.1, 79.8, -13.64, 5.09]))