'''Q27: Write a program to print the sum of the first n odd numbers.
Sample Test Cases:
Input 1:
3
Output 1:
9
Input 2:
5
Output 2:
25'''
n=int(input("enter n:"))
s=0
for i in range(1,n+1,1):
        s=(2*i-1)+s
print(s)
