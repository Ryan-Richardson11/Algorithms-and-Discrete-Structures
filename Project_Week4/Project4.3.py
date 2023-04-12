# Input: A positive integer n and two nxn matrices of numbers.
# Output: Returns the product of the two nxn matrices.
def multiply_matrices(n, A, B):
    # Creates a matrix of size n, 0 initialized to all indices.
    ans = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # Multiply the i-th row of A and the j-th column of B and add it to that index.
                ans[i][j] += A[i][k] * B[k][j]
    return ans
    

test_one = multiply_matrices(2, [[2, 7], [3, 5]], [[8, -4], [6, 6]])
for row in test_one:
    print(row)

test_two = multiply_matrices(3, [[1, 0, 2], [3, -2, 5], [6, 2, -3]], [[0.3, 0.25, 0.1], [0.4, 0.8, 0], [-0.5, 0.75, 0.6]])
for row in test_two:
    print(row)