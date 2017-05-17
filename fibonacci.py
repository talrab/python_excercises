

run_loop = True
num_elements = int(input("Please enter the number of elements: "))
if num_elements < 0:
    run_loop = False
while (run_loop):
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
    num_elements = int(input("Please enter the number of elements: "))
    if num_elements < 0:
        run_loop = False




# a 'classier' solution to find the nth element of fibonacchi:
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,b+a
    return a

print(fib(5))






