def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num = int(input("Enter the number"))
if num<0:
    print("Factorial doesn't exits for negative number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of",num,"is",factorial(num))

    
