'''Q22: Write a program to find profit or loss percentage given cost price and selling price.

/*
Sample Test Cases:
Input 1:
1000 1200
Output 1:
Profit 20%

Input 2:
1000 800
Output 2:
Loss 20%

Input 3:
1000 1000
Output 3:
No Profit No Loss'''
cp=int(input("enter cp:"))
sp=int(input("entr sp:"))
if (cp>sp):
    print("Loss",((cp-sp)/cp)*100,"%")
elif (cp==sp):
    print("No Profit No Loss")
else:
     print("Profit",((sp-cp)/cp)*100,"%")
    

