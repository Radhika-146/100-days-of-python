'''Q33: Write a program to check if a number is an Armstrong number.
Sample Test Cases:
Input 1:
153
Output 1:
Armstrong

Input 2:
123
Output 2:
Not Armstrong'''
n=int(input("enter a number:"))
temp=n
real_num=n
c=0
while(temp!=0):
    d=temp%10
    c=c+1
    temp=temp//10
num=0
while(n!=0):
    x=n%10
    num=num+(x**c)
    n=n//10
if (real_num==num):
    print("Armstrong")
else:
    print("Not Armstrong")
