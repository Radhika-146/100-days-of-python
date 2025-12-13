'''Q6: Write a program to swap two numbers using a third variable.
Sample Test Cases:
Input 1:
3 5
Output 1:
After swap: 5 3

Input 2:
-1 1
Output 2:
After swap: 1 -1'''

a=int(input("enter a number: "))
b=int(input("enter another number: "))
temp=a
a=b
b=temp
print("After swap: ",a,b)
