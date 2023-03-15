"""
Defines a function called vector_swap()

Holds the parameter vector which its iterated through and swaps adjacents values with each other.
"""
def vector_swap(vector):
    # iterates through for each index in 0 to the lenght of the vector while jumping by 2.
    for i in range(0, len(vector), 2):
        # Swapps each vector for the the one that comes directly after it.
        vector[i], vector[i+1] = vector[i+1], vector[i]
    return vector
# Creates a variable new_num that will take an input based on the conditions set.
new_num = int(input("Please enter an even number between 9 and 21: "))
if new_num % 2 != 0 or new_num < 9 or new_num > 21:
    print("Invalid input")
else:
    # the vector will be a list with the length of the input value.
    vector = list(range(new_num))
    # new_vector is created and vector_swap is called with the parameter vector defined above it.
    new_vector = vector_swap(vector)
    print(new_vector)
