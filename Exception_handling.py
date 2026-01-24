def f1(dv1,dvr):
    q=dv1/dvr
    return q
def f2(num):
    print('the given integer number is:',num)
print()
try:
    a=int(input('Enter the divident: '))
    b=int(input('Enter the divisor: '))
    c=f1(a,b)
    if c:
        print('the quotient is:',c)

except:
    print('Arthimaticerror')
    print('Sorry,no number can be divided by zero')

print()

try:
    d=int(input('Enter the integer number: '))
    f2(d)
    print('the given integer number is: ',d)

except:
    print('valueerror')
    print('only integer number can be allowed')