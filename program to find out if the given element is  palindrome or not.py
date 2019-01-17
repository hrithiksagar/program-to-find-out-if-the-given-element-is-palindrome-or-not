#palindrome or not
x=input("enter any word to check if its a palindrome")
x2=x[::-1]
if x==x2:
    print("yes")
else:
    print("no")     
