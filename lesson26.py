#Write a program to calculate the sum of whole numbers

y=int(input("enter the number"))

sum=0
for i in range(0,y+1):
    sum=sum+i
    print("\n Sum :", sum)