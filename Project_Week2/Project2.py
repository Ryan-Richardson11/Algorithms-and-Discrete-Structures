class person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age  = age
    def getName(self):
        return self.name
    def getFullName(self):
        return self.name+" "+self.famN
    def getFamilyName(self):
        return self.famN
    def getAge(self):
        return self.age
    
class Stack():
    
    def __init__(self):
        self.items = []

    def add_end(self, item):
        self.items.append(item)
    
    def remove_end(self):
        self.items.pop()
    
    def display_items(self):
        return self.items

def readPeople(fileName):
    infile = open(fileName, "r")
    people = {}
    for line in infile:
        info = line.split(",")
        people.update({info[0]:person(info[1], info[2], int(info[3]))})
    return people

def printPeople(people):
    print("==========================")
    print(" Nickname  Name           ")
    print("==========================")
    for k in people.keys():
        print("{0:>9}  {1:<15}".format(k,people[k].getFullName()))

def main():
    fileName = input("Enter the file name with people info: ")
    everyone = readPeople(fileName)
    printPeople(everyone)

    print("==========================")
    print("Current Stack:")
    print("==========================")

    stack = Stack()
    for key in everyone.keys():
        stack.add_end(key)
    print(stack.display_items())

    while stack.items:
        try:
            remove_people = eval(input("Please enter a random number from 1 to 4: "))
            if remove_people > len(stack.items):
                print(f"Invalid input. Input is greater than stack length. {len(stack.items)} items left.")
            elif remove_people >= 1 and remove_people <= 4:
                for i in range(remove_people):
                    stack.remove_end()
                print(stack.display_items())
            else:
                print("Invalid. The input must be from 1 to 4.")
        except:
            print("Invalid input.")
    print("The stack is empty.")
    return None
    
main()


# class Stack():
    
#     def __init__(self):
#         self.items = []

#     def add_end(self, item):
#         self.items.append(item)
    
#     def remove_end(self):
#         self.items.pop()
    
#     def display_items(self):
#         return self.items

# stack = Stack()
# stack.add_end("apple")
# stack.add_end("banana")
# stack.add_end("orange")
# stack.add_end("grape")
# stack.add_end("plum")
# print(stack.display_items())
# stack.remove_end()
# print(stack.display_items())

    
    