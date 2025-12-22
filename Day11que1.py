'''Q21: Write a program to display the month name and number of days using switch-case for a given month number.

/*
Sample Test Cases:
Input 1:
2
Output 1:
February, 28 days

Input 2:
12
Output 2:
December, 31 days'''
n=int(input("enter num:"))
match n:
    case 1:
        print("January, 31 days")
    case 2:
        print("February, 28 days")
    case 3:
        print("March, 31 days")
    case 4:
        print("April, 30 days")
    case 5:
        print("May, 31 days")
    case 6:
        print("June, 30 days")
    case 7:
        print("July, 31 days")
    case 8:
        print("August, 31 days")
    case 9:
        print("September, 30 days")
    case 10:
        print("October, 31 days")
    case 11:
        print("November, 30 days")
    case 12:
        print("December, 31 days")
    case _:
        print("Invalid month number")
