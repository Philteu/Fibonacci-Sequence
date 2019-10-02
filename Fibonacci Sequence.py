

#Fibonacci Sequence
def Fibonacci(n):
    if n < 0:
        print('Invalid Input')
    elif n <= 1:
        return n
    else:
        return (Fibonacci(n-1)+ Fibonacci(n - 2 )) #F= Fn-1 + Fn-2

n= int(input('This is Fibonacci Sequence. Enter the iteration: '))
for i in range(n):
    print(Fibonacci(i))
    
#0,1,1,2,3,5,8,13,21,34,55