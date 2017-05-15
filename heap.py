################################################################
# Write a Python program to push three items into the heap and
# print the items from the heap. Go to the editor
################################################################

import heapq

heap = []
heapq.heappush(heap,'4')
heapq.heappush(heap,'9')
heapq.heappush(heap,'2')
heapq.heappush(heap,'5')
heapq.heappush(heap,'1')
heapq.heappush(heap,'7')

for a in heap:
    print(a)

# return the smallest item in the heap
print ("The smallest item is: " + heap[0])

for _ in range(len(heap)):
    print ("Popping the smallest item: " + heapq.heappop(heap))

heap = []
heapq.heappush(heap,'4')
heapq.heappush(heap,'9')
heapq.heappush(heap,'2')
heapq.heappush(heap,'5')
heapq.heappush(heap,'1')
heapq.heappush(heap,'7')

for a in heap:
    print(a)

# pushing an item and popping the smallest out
heapq.heappushpop(heap,'6')
for _ in range(len(heap)):
    print ("Popping the smallest item: " + heapq.heappop(heap))
