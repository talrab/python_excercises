###################################################################
# Question:
# when given a sorted array and a sum number you need to see
# whether there is a pair in this list with this sum
# you need to do it in O(n)
# Answer:
# always look at the right most and left most indexes and calucalte their sum
# if their sum is smaller than the needed one, move the left one,
# if their sum is bigger, move the right one
# if it is the same sum, you doing your answer.
# do it until you have an answer or the indexes reach each other
###################################################################

class Answer:
    l_index = 0
    r_index = 0
    l_value = 0
    r_value = 0
    hasSum = False


sorted_array = [-2,-1,4,5,8,12,14]
sum = 2

def findSum (needed_sum):
    left_index = 0
    right_index = len(sorted_array) - 1
    while (left_index < right_index):
        left_value = sorted_array[left_index]
        right_value = sorted_array[right_index]
        if (left_value + right_value == needed_sum):
            answer = Answer()
            Answer.hasSum = True
            Answer.l_index = left_index
            Answer.r_index = right_index
            Answer.l_value = left_value
            Answer.r_value = right_value
            return answer
        elif (left_value + right_value < needed_sum):
            left_index += 1
        elif (left_value + right_value > needed_sum):
            right_index -= 1


ans = findSum(sum)

print(ans.hasSum)
print("Left value = " + str(ans.l_value))
print("Right value = " + str(ans.r_value))





