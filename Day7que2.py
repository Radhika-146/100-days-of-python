'''Q14: Write a program to input a character and check whether it is a vowel or consonant using if–else.

/*
Sample Test Cases:
Input 1:
a
Output 1:
Vowel

Input 2:
b
Output 2:
Consonant'''
c=input("enter character:").lower()
for i in ("a","e","i","o","u"):
    if (c==i):
        print("Vowel")
        break
    else:
        print("Consonant")
        break
