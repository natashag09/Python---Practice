# For Loop (Iteration with range)


#Q Display counting till number input
n = int(input('enter number:'))
for i in range(1,n+1):
    print(i)
            
#Q Sum of 1 to n 
n = int(input('enter n'))
s=0 
for i in range(1,n+1):
    s=s+i
print(s)

#Q Average of 1 to n 
n = int(input('enter n'))
s=0
for i in range(1,n+1):
    s=s+i
print(s/n)

#Q Calculate average of even and odd numbers 
n = int(input('enter n'))
ce = 0
se = 0

co = 0
so = 0
for i in range(1,n+1):
    if i%2 == 0:
        ce = ce+1
        se = se+i
    else:
        co = co+1
        so = so+i
print(se/ce)
print(so/co)

#Q Print table of n 
n = int(input('enter n'))
for i in range(1,11):
    print(n,'*',i ,'=',n*i)

#Q Print factorial of n 
n = int(input('enter n'))
f = 1
for i in range(1,n+1):
    f = f*i
print(f)

#Q Prime or not Prime
n = int(input('enter n'))
c = 0
for i in range(1,n+1):
    if n%i == 0:
        c = c+1
if c == 2:
    print(n,'is prime')
else:
    print(n,'is not prime')

#Q Ask no. of inputs equal to n and then calculate average of those inputs
n = int(input('enter n'))
s = 0
for i in range(1,n+1):
    a = int(input('enter a'))
    s = s+a
print(s/n)

#Q Print Fibonacci series 
n = int(input('enter n'))
a = 0
b = 1
for i in range(1,n+1):
    print(a)
    c = a
    a = b
    b = c+a 