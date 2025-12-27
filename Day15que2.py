'''Q30: Write a program to reverse a given number.
Sample Test Cases:
Input 1:
1234
Output 1:
4321

Input 2:
100
Output 2:
1'''
n=int(input("enter a number:"))
temp=n
rev=0
while(temp!=0):
    d=temp%10
    rev=rev*10+d
    temp=temp//10
print(rev)
