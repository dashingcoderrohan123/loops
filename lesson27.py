#Write a program to reverse the string entered by the user.

g=str(input("enter the string:"))

string2=("")

for h in g:
    string2=h+string2

print("\n Original string is :",g)
print("reversed string is:",string2)
