######################################################################################
# Python program to create a queue and display all the members and size of the queue.
######################################################################################

from Lib import queue

print ("*** FIFO ***")
fifo_q = queue.Queue()
fifo_q.put(1)
fifo_q.put(3)
fifo_q.put(5)
fifo_q.put(7)

print ("The Queue is empty: " + str(fifo_q.empty()))

print ("Queue size: " + str(fifo_q.qsize()))
print ("Queue items: ")
for _ in range(fifo_q.qsize()):
    print(fifo_q.get())

print ("The Queue is empty: " + str(fifo_q.empty()))

print ("\n*** LIFO ***")

lifo_q = queue.LifoQueue()
lifo_q.put(1)
lifo_q.put(3)
lifo_q.put(5)
lifo_q.put(7)

print ("The Queue is empty: " + str(lifo_q.empty()))

print ("Queue size: " + str(lifo_q.qsize()))
print ("Queue items: ")
for _ in range(lifo_q.qsize()):
    print(lifo_q.get())

print ("The Queue is empty: " + str(lifo_q.empty()))
