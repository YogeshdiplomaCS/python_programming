num=int(input("Enter the number:"))
print('the given number is:',num)

fact=1

if num<0:
    print('the given number cannot be negative')
elif num==0:
    print('the given number cannot be 0')
else:
    while num>0:
        fact=fact*num
        num=num-1
        print('the factorial of the given number is:',fact)