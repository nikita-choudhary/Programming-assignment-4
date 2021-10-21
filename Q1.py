#1.	Write a Python Program to Find the Factorial of a Number?
n=int(input("Enter the no.: "))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(f"the factorial of {n} is {factorial(n)}")



