'''Q31: Write a program to take a number as input and print its equivalent binary representation.
Sample Test Cases:
Input 1:
10
Output 1:
1010

Input 2:
7
Output 2:
111'''

n=int(input("enter a number:"))
b=1
while (n!=0):
    d=n%2
    b=b*10+d
    n=n//2
print(b)

