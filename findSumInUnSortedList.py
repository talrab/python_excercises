####################################################
# Find a pair of elements from a given array whose
# sum equals a specific target number.
# In O(n)
####################################################


a=(10,20,10,40,50,60,70)
target = 110

reminder={}
answer=()

for i, n in enumerate(a):
    r = target-n
    if n in reminder:
        answer=(reminder[n],i)
    reminder[r]=i

if answer:
    print ("The list is = ")
    print (a)
    print ("The target sum is: " + str(target))
    print ("The numbers are: a[" + str(answer[0]) + "]=" + str(a[answer[0]]) + " a[" + str(answer[1]) + "]=" + str(a[answer[1]]))
else:
    print ("Target sum doesn't exist")






