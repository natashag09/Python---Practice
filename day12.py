# Control Statements and Nested Loop

#Q Iterate through a string and skip a specific character using continue, print a message for others
n = 'deepanshu'
for i in n:
    if i == 'a':
        continue
    print('hello')
print(i)

#Q Use a loop to calculate sum and skip a specific value using continue while printing intermediate values
s=0
for c in range(1,9):
    s = s+c
    c = c+1
    if c == 5:
        continue
    print('c is:', c)
print('sum is:', s)

#Q Take a number as input and check if it is even or odd using if-else (use pass for one condition)
n = int(input('enter n:'))
if n%2 == 0:
    print('even')
else:
    pass 

#Q use nested loops to print numbers in a simple pattern
for i in range(1,3):
    for j in range(1,3):
        print(j)

#Q Use nested loops to print increasing sequence based on outer loop value
for i in range(3):
    for j in range(1,i):
        print(j)

#Q Print multiplication tables from 1 to n using nested loops
n = int(input('enter n:'))
for i in range(1,n+1):
    print('Table of ', i,'\n')
    for j in range(1,11):
        print(i, '*', j, '=', i*j)

#Q Print multiplication tables from 1 to n using nested loops
L = ['c','python','java','perl','ruby','pascal']
for i in L:
    for j in i:
        if j == 'p':
            print(i)
