##########################################################################
##########################################################################
#
# Exercises from -
# http://www.w3resource.com/python-exercises/challenges/1/index.php
#
##########################################################################
##########################################################################



##########################################################################
# Exec 10
# Write a Python program to find three numbers from an array such that
# the sum of three numbers equal to a given number.
# Input : [1, 0, -1, 0, -2, 2], 0)
# Output :  [[1,0,-1],[1,-1,0],[0,-2,2]]
##########################################################################
print ("\n\nExec 10\n")

l = [1, 0, -1, 0, -2, 2]
target_sum = 0
answer=[]

first = 0
second = first +1
third = second +1
while first <= len(l)-3:
    second = first + 1
    third = second + 1
    while second <= len(l)-2:
        third = second + 1
        while third <= len(l)-1:
            sum = l[first]+l[second]+l[third]
            if sum == target_sum:
                answer.append([l[first], l[second], l[third]])
            third += 1
        second += 1
    first += 1

print(answer)




##########################################################################
# Exec 18
# Write a Python program to reverse the digits of an integer.
# Input : 234
# Input : -234
# Output: 432
# Output: -432
##########################################################################
print ("\n\nExec 18\n")

a = -2340
if a<0:
    sign = -1
else:
    sign = 1

list_a = list(str(a))
if sign == -1:
    list_a = list_a[1:]
list_a.reverse()
x = "".join(list_a)
print (int(x)*sign)



##########################################################################
# Exec 20
# Write a Python program to check a sequence of numbers is an arithmetic progression or not.
# Input : [5, 7, 9, 11]
# Output : True
# In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers
# such that the difference between the consecutive terms is constant.
##########################################################################
print ("\n\nExec 20\n")

a = [5, 7, 9, 11, 13, 15]
b = [5, 7, 9, 11, 12, 15]

def isProgression (list):
    dif = list[1] - list[0]
    for i in range(len(list)-1):
        if (list[i+1] - list[i] != dif):
            return False
    return True


print (isProgression(a))
print (isProgression(b))



##########################################################################
# Exec 23
# Write a Python program where you take any positive integer n,
# if n is even, divide it by 2 to get n / 2.
# If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
# Repeat the process until you reach 1.
# Input : 12
# Output : [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
##########################################################################
print ("\n\nExec 23\n")

n = 19
answer = []
answer.append (n)
while n != 1:
    if n%2 == 0:
        n = n/2
    else:
        n=n*3+1
    answer.append(n)
print (answer)




##########################################################################
# Exec 26
# is a given string an anagram of another string
# an 'anagram' is when a word is written with exactly the same letters
##########################################################################
print ("\n\nExec 26\n")

from collections import Counter

a = "anagram"
b = "nagaram"

print(Counter(a))
print(Counter(b))
print (Counter(a) == Counter(b))


##########################################################################
# Exec 30
# Write a Python program to find the length of the last word.
##########################################################################
print ("\n\nExec 30\n")

a = 'Python Exercises'
b = a.split()
last_word = b[len(b)-1]
print ("Last word is: '" + last_word + "'")
print ("Last word length is: " + str(len(list(last_word))))



