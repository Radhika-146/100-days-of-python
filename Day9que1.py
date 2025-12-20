'''Q17: Write a program to find the roots of a quadratic equation and categorize them.
Sample Test Cases:
Input 1:
1 -3 2
Output 1:
Roots are real and different: 2, 1

Input 2:
1 -2 1
Output 2:
Roots are real and same: 1

Input 3:
1 2 5
Output 3:
Roots are complex'''
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
x=(b**2-4*a*c)
if(x>0):
    d=x**(1/2)
    r1=(-b+d)/(2*a)
    r2=(-b-d)/(2*a)
    print("Roots are real and different: ",int(r1), ",",int(r2))
elif(x==0):
    d=x**(1/2)
    r1=(-b+d)/(2*a)
    r2=(-b-d)/(2*a)
    print("Roots are real and same: ",int(r1))
else:
    print("Roots are complex ")

    
