'''Q34: Write a program to check if a number is prime.
Sample Test Cases:
Input 1:
7
Output 1:
Prime

Input 2:
10
Output 2:
Not prime'''
n=int(input("enter num:"))
d=0
for i in range(1,n+1):
    if(n%i==0):
        d+=1
if(d==2):
    print("Prime")
else:
    print("Not prime")
