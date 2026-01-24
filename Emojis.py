import emoji
import math

x=eval(input('Enter the first number: '))
y=eval(input('Enter the second number: '))
print('the given numbers are %d and %d'%(x,y))

str1='MATH MODULE OPERATIONS'
print(str1.center(50,'*'))

print('square root of first number is ',math.sqrt(x))
print('square root of second number is ',math.sqrt(y))
z=math.pow(x,y)
print('value of %d ^ %d is %d'%(x,y,z))
print()

str2='EMOJI MODULE OPERATIONS'
print(str2.center(50,'*'))
a=emoji.emojize(':skull:')
b=emoji.emojize(':grinning_face:')
c=emoji.emojize(':beaming_face_with_smiling_eyes:')
d=emoji.emojize(':baby:')
print('skull:',a)
print('grinning_face:',b)
print('beaming_face_with_smiling_eyes:',c)
print('baby_face:',d)
print()

q=emoji.demojize(':😀:')
w=emoji.demojize(':💀:')
print('CDLR short name of 💀is:',q )
print('CDLR short name of 😀 is:',w )