'''Q18: Write a program that accepts a percentage (0-100) and assigns a grade based on the following criteria: 
90-100: Grade A 
80-89: Grade B 
70-79: Grade C 
60-69: Grade D 
below 60: Grade F.
Sample Test Cases:
Input 1:
95
Output 1:
Grade A

Input 2:
82
Output 2:
Grade B

Input 3:
68
Output 3:
Grade D

Input 4:
50
Output 4:
Grade F'''
m=int(input("enter marks in  percentage: "))
if (m>=90):
    print("Grade A")
elif (m>79 and m<90):
    print("Grade B")
elif (m>69 and m<80):
    print("Grade C")
elif(m>59 and m<70): 
    print("Grade D")
else:
    print("Grade F")
