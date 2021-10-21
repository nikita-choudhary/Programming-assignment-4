#4.	Write a Python Program to Check Armstrong Number?
n = int(input("Enter the number : "))
sum=0
t=n
while t!=0:
    digit =t%10
    sum=sum+digit**3
    t=t//10

if sum==n:
    print("It is an armstrong number")
elif sum!=n:
    print("Not an armstrong")


