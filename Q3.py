#3.	Write a Python Program to Print the Fibonacci sequence?
num= int(input("Enter the number: "))
f=[0,1]
def fibbo(num):
    for i in range(2,num):
        f.append(f[i-1]+f[i-2])

fibbo(num)
print(f)
print(f[-1])



