#5.	Write a Python Program to Find Armstrong Number in an Interval?
l= int(input("Enter the lower range : "))
u = int(input("Enter the upper range : "))

for i in range(l,u+1):
    t=i
    sum=0
    while t!=0:
        digit=t%10
        sum=sum+digit**3
        t=t//10
    if i==sum:
        print(i)

