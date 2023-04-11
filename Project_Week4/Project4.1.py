# Input: An array of integers and a positive number
# Output: Returns the integers in the array that are divisible by the given number
def is_it_divisible(array, number):
    nums_divisible = []
    for i in array:
        if i % number == 0:
            # Adds i to the list if its value is divisible by the given number.
            nums_divisible.append(i)
    return nums_divisible
        
print(is_it_divisible([20, 21, 25, 28, 33, 34, 35, 36, 41, 42], 7))
print(is_it_divisible([18, 54, 76, 81, 36, 48, 99], 9))