#####################################################################
# a Python program to convert an array to an ordinary list with the
# same items.
#####################################################################

from array import array

a = array('b', {1, 3, 5, 7, 9})
list =[]
for item in a:
    list.append(item)
print (list)

# a better approach:
list = a.tolist()
print (list)


