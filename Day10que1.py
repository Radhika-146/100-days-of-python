'''Q19: Write a program to classify a triangle as Equilateral, Isosceles, or Scalene based on its side lengths.

/*
Sample Test Cases:
Input 1:
3 3 3
Output 1:
Equilateral

Input 2:
3 3 4
Output 2:
Isosceles

Input 3:
2 3 4
Output 3:
Scalene'''
s1=int(input("side1:"))
s2=int(input("side2: "))
s3=int(input("side3:"))
if (s1==s2==s3):
    print("Equilateral")
elif(s1==s2 or s2==s3 or s3==s1):
    print("Isosceles")
else:
    print("Scalene")
