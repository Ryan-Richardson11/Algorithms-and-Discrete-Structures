# Input: An x value and the p power it is being raised to.
# Output: returns a calculation of x*x p times.
def power(x, p):
    ans = 1
    for i in range(p):
        # Starts at 1 then multiplies x by itself p times when the function is called.
        ans *= x
    return ans
# Input: An array A of integers in a polynomial and a given x value.
# Output: A solved polynomial where the index represented the power of x.
def evaluate(A, x):
    polynomial_length = len(A)
    # Initializes the solved value to zero.
    solved = 0
    for i in range(polynomial_length):
        # For the length of the array x is raised to the index of A.
        power_raised = A[i] * power(x, i)
        # Adds power raised to solved as it iterates through the array.
        solved += power_raised
    return f"{solved:.2f}"


A = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]
x = 5.4
print(evaluate(A, x))
