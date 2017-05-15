################################################################
# Write a Python program to group a sequence of key-value pairs
# into a dictionary of lists.
# Input:
# [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 1)]
# Expected output:
# [('a', [1, 3]), ('b', [2, 4]), ('c', [1])]
################################################################

from collections import defaultdict

tuple_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 1),('c', 5),('a', 5)]

dicOfLists=defaultdict(list)

for k,v in tuple_list:
    dicOfLists[k].append(v)

print(sorted(dicOfLists.items()))






