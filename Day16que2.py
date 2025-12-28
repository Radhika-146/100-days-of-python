'''Q32: Write a program to check if a number is a palindrome.

/*
Sample Test Cases:
Input 1:
121
Output 1:
Palindrome

Input 2:
123
Output 2:
Not palindrome'''
n=int(input("enter a number:"))
temp=n
rev=0
while(temp!=0):
    d=temp%10
    rev=rev*10+d
    temp=temp//10
if (rev==n):
    print("Palindrome")
else:
    print("Not Palindrome")
  
