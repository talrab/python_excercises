
# Write a Python program to sort a dictionary and print the members of the dictionary in reverse order.



dic = {"a":3, "c":7, "b":1, "g":2, "d":9}
#sorted
ordered = sorted(dic.items(), key=lambda t: t[0])
print(ordered)
for k,v in ordered:
    print (k + " " + str(v))

#in reverse
ordered = sorted(dic.items(), key=lambda t: t[0],reverse=True)
print(ordered)
for k,v in ordered:
    print (k + " " + str(v))
