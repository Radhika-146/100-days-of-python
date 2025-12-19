'''Q16: Write a program to input three numbers and find the largest among them using if–else.

Sample Test Cases:
Input 1:
3 7 5
Output 1:
Largest is 7

Input 2:
-1 -5 0
Output 2:
Largest is 0'''

a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))
if (a>b and a>c):
    print("Largest is",a)
elif (b>a and b>c):
    print("Largest is",b)
else:
    print("Largest is",c)   
