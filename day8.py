# While Loop (Problem Solving)

#Q Take a number n as input and calculate the average of numbers from 1 to n
n = int(input('enter n'))
c=0
s=0
while c<n:
    c=c+1
    s=s+c
print(s/n)


#Q Take a number n and calculate:
# - count and sum of squares of even numbers
# - count and sum of cubes of odd numbers
# from 1 to n using while loop

n = int(input('enter n'))
c=0

ce=0
se=0

co=0
so=0

while c<n:
    c=c+1
    if c%2 == 0:
        ce = ce+1
        se = se+c**2
    else:
        co = co+1
        so = so+c**3
print(ce,se)
print(co,so)


#Q Take a number n as input and print its multiplication table up to 10 
n = int(input('enter n'))
c=0
while c<10:
    c = c+1
    print(n, '*', c, '=', n*c)


#Q Take a number n as input and calculate its factorial 
n = int(input('enter n'))
c=0
f=1
while c<n:
    c=c+1
    f=f*c
print(f)


#Q Take a number n as input and check whether it is a prime number or not
n = int(input('enter n'))
c=0
f=0
while c<n:
    c=c+1
    if n%c == 0:
        f=f+1
if f == 2:
    print('prime')
else:
    print('not prime')


#Q Take n inputs from the user and calculate their average
n = int(input('enter n'))
c=0
s=0
while c<n:
    c=c+1
    a=int(input('enter a'))
    s=s+a
print(s/n)    