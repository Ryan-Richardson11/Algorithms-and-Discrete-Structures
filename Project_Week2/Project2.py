class person:
    """
    Creates the class person

    Creates the attribute varibles self.name, self.famN and self.age
    """
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age  = age
    """
    Creates the initializer method for the person class

    Parameters: name, familyName, age
    """
    def getName(self):
        return self.name
    """
    Creates getName method

    Returns the first name.
    """
    def getFullName(self):
        return self.name+" "+self.famN
    """
    Creates getFullName method

    Returns the first name and the last name.
    """
    def getFamilyName(self):
        return self.famN
    """
    Creates getFamilyName method

    Returns the last name.
    """
    def getAge(self):
        return self.age
    """
    Creates getAge method

    Returns the age.
    """

class Stack():
    """
    Creates the class Stack

    Creates a list and methods to function as a stack data structure.
    """
    def __init__(self):
        self.items = []
    """
    Creates the initializer method for the Stack class

    Creates an empty list called self.items
    """
    def add_end(self, item):
        self.items.append(item)
    """
    Creates add_end method

    Takes an item as an argument and adds that item to the end of the stack.
    """
    def remove_end(self):
        self.items.pop()
    """
    Creates remove_end method

    Removes the item currently at the end or top of the stack. (The last item to be entered into the stack).
    """
    def next_popped(self):
        return self.items[-1]
    """
    Creates next_popped method

    Returns the item currently at the end or top of the stack.
    """
def readPeople(fileName):
    """
    Creates readPeople method

    Reads the people.csv file or any other passed as an argument and creates an empty dictionary called people.
    """
    infile = open(fileName, "r")
    people = {}
    for line in infile:
        info = line.split(",")
        # Adds the data from the person.csv file into the people dictionary as separate objects
        people.update({info[0]:person(info[1], info[2], int(info[3]))})
    return people

def printPeople(people):
    """
    Creates printPeople method

    Prints out dictionary objects keys, which are their nicknames, followed by calling the getFullName method to get each objects first
    and last name to print out.
    """
    print("==========================")
    print(" Nickname  Name           ")
    print("==========================")
    for k in people.keys():
        print("{0:>9}  {1:<15}".format(k,people[k].getFullName()))

def main():
    """
    Creates main method

    Calls previous methods to store objects into a stack and perform functions on them.
    """
    # Asks for the file to be read by the readPeople method and stores it in the variable "everyone".
    fileName = input("Enter the file name with people info: ")
    everyone = readPeople(fileName)
    # Calls the printPeople method on the variable everyone to retrieve the necessary data to print.
    printPeople(everyone)

    print("=============")
    print("Top of Stack:")
    print("=============")

    # Instatiates the stack object and creates an instace of the Stack class.
    stack = Stack()
    # Itterates through each key in the dictionary that is now everyone and adds those keys to the end of the stack.
    for key in everyone.keys():
        stack.add_end(key)
    print(stack.next_popped())

    # While the stack is not empty
    while stack.items:
        try:
            # User inputs a value from 1 to 4 called remove_people
            remove_people = eval(input("Please enter a random number from 1 to 4: "))
            # Invalid input if the user input is greater than the items present.
            if remove_people > len(stack.items):
                print(f"Invalid input. Input is greater than stack length. {len(stack.items)} item(s) left.")
            # If the input is valid, itterates through and removes amount of people based on the input.
            elif remove_people >= 1 and remove_people <= 4:
                for i in range(remove_people):
                    stack.remove_end()
                print("=============")
                print("Top of Stack:")
                print("=============")
                # Prints the next person in the stack that will be removed.
                print(stack.next_popped())
            else:
                print("Invalid. The input must be from 1 to 4.")
        except:
            if not stack.items:
                break
            print("Invalid input. Input must be an integer.")
    # When the stack is out of items the program will return None.
    print("The stack is empty.")
    return None
    
main()


    
    