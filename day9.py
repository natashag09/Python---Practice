# While Loop (Number-Based Problem Solving)

#Q Take a number as input and count the number of digits
n = int(input('enter n:'))
c=0
while n>0:
    c=c+1
    n= n//10
print(c)


#Q Take a number as input and reverse it 
n = int(input('enter n:'))
rev = 0
while n>0:
    d = n%10
    rev = rev*10+d
    n = n//10 
print(rev)


#Q Take a number as input and check whether it is a palindrome or not
n = int(input('enter n:'))
a=n
rev = 0
while n>0:
    d = n%10
    rev = rev*10+d
    n = n//10 
if a == rev:
    print('palindrome')
else:
    print('not palindrome')


#Q Take a number as input and check whether it is an Armstrong number or not
n = int(input('enter n:'))
a=n
b=a
arm=0
c=0
while n>0:
    c = c+1
    n = n//10
print(c)
while a>0:
    d = a%10
    arm = arm + d**c
    a = a//10 
if arm == b:
    print(b,'is armstrong')
else:
    print(b,'is not armstrong')


#Q Take a number n and print first n terms of Fibonacci series 
n = int(input('enter n'))
a=0
b=1
y=0
while y<n:
    print(a)
    c = a
    a = b
    b = c+a
    y = y+1