import queue

my_queue = queue.Queue()
my_queue.put("apple")
my_queue.put("banana")
my_queue.put("peach")
my_queue.put("plum")

item1 = my_queue.get()
print(item1)
item2 = my_queue.get()
print(item2)


