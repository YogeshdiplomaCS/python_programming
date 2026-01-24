nterms=int(input("enter the terms of fibonacci series:"))

str1='FIBONACCI SERIES'
print(str1.center(50,'*'))

num1=0
num2=1

for i in range(nterms):
    num=num1+num2
    print(num1,end=' ')
    num1=num2
    num2=num