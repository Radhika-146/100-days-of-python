'''Q11: Write a program to input an integer and check whether it is even or odd using if–else.

/*
Sample Test Cases:
Input 1:
7
Output 1:
7 is odd

Input 2:
12
Output 2:
12 is even'''
n=int(input("enter number: "))
if (n%2==0):
   print(n,"is even")
else:
   print(n,"is odd")
