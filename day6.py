# Problem Solving (using iteration)


#Q Print numbers from n to 1 (reverse)
n = int(input('enter n: '))
for i in range(n, 0, -1):
    print(i)


#Q Count digits in a number
n = int(input('enter number: '))
count = 0

for i in str(n):
    count += 1

print(count)


#Q Reverse a string
s = input('enter string: ')
rev = ""

for i in s:
    rev = i + rev

print(rev)


#Q Check palindrome
s = input('enter string: ')
rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print('Palindrome')
else:
    print('Not Palindrome')