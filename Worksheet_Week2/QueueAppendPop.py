class queue:
    
    def __init__(self):
        self.q = []

    def insert_end(self, item):
        self.q.append(item)

    def remove_beginning(self):
        self.q.pop(0)

    def display(self):
        return self.q
def main():

    my_queue = queue()
    my_queue.insert_end("a")
    my_queue.insert_end("b")
    my_queue.insert_end("c")
    my_queue.insert_end("d")
    my_queue.insert_end("e")
    print(my_queue.display())
    my_queue.remove_beginning()
    print(my_queue.display())
main()