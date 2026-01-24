str1=input("Enter a string:")
print('the given string is',str1)
rev_str=str1[::-1]
if str1==rev_str:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")