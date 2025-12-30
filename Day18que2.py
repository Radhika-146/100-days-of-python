'''Q36: Write a program to find the HCF (GCD) of two numbers.
Sample Test Cases:
Input 1:
12 18
Output 1:
6
Input 2:
7 9
Output 2:
1'''
n1=int(input("enter num1:"))
n2=int(input("enter num2:"))
if (n1>n2):
    x=n1
else:
    x=n2
for i in range(1,x+1):
    if(n1%i==0):
        if(n2%i==0):
            gcd=i
print(gcd)
