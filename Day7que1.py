'''Q13: Write a program to input a year and check whether it is a leap year or not using conditional statements.

/*
Sample Test Cases:
Input 1:
2020
Output 1:
Leap year

Input 2:
1900
Output 2:
Not a leap year

Input 3:
2000
Output 3:
Leap year'''
y=int(input("enter year:"))
if ( y%100==0 and y%400==0):
    print("Leap Year")
else: 
    if ( y%100!=0 and y%4==0):
       print("Leap year")
    else:
       print("Not a leap year")

