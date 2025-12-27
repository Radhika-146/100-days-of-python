'''Q29: Write a program to calculate the factorial of a number.
Sample Test Cases:
Input 1:
5
Output 1:
120

Input 2:
3
Output 2:
6'''
n=int(input("enter num:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print (fact)
