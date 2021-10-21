#6.	Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("Enter the nth number : "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"The sum of {n} natural numbers is {sum}")
    