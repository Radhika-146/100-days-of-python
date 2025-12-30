'''Q35: Write a program to print all factors of a given number.
Sample Test Cases:
Input 1:
6
Output 1:
1 2 3 6

Input 2:
10
Output 2:
1 2 5 10'''
n=int(input("enter a number:"))
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=' ')
