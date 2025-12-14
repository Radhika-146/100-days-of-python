'''
Q8: Write a program to find and display the sum of the first n natural numbers.

/*
Sample Test Cases:
Input 1:
5
Output 1:
Sum=15

Input 2:
10
Output 2:
Sum=55'''
n=int(input("enter the number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum=",sum)  
