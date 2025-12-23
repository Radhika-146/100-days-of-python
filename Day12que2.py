'''Q24: Write a program to calculate electricity bill based on units consumed with these rates: 
First 100 units at ₹5/unit 
Next 100 units at ₹7/unit 
Next 100 units at ₹10/unit 
Above at ₹12/unit

/*
Sample Test Cases:
Input 1:
50
Output 1:
Bill: ₹250

Input 2:
150
Output 2:
Bill: ₹850

Input 3:
250
Output 3:
Bill: ₹1700'''

u=int(input("enter units:"))
if(u<=100):
    b=u*5
    print("Bill: ₹",b)
elif(u>=101 and u<=200):
    b=500+(u-100)*7
    print("Bill: ₹",b)
elif(u>=201 and u<=300):
    b=500+700+(u-200)*10
    print("Bill: ₹",b)
else:
    b=500+700+1000+(u-300)*12
    print("Bill: ₹",b)
