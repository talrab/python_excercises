
while (True):
    num_elements = int(input("Please enter the number of elements: "))
    answer = []

    for x in range(num_elements):
        print( "X=" + str(x))
        if (x+1==1):
            answer.append(1)
        elif (x+1==2):
            answer.append(1)
        else:
            answer.append (answer[x-2] + answer[x-1])

    print (answer)