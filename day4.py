# For Loop (Iterating in given iterable)

#Q String input , print character by character
s = input('enter string:') 
for i in s: 
    print(i) 
print('bye') 

#Q Count the character of string 
s = 'aman'
c=0
for i in s: 
    c=c+1 
print(c)

#Q Count total no of elements in the list 
L = [1,2,3,4,5,6,7,8,9,0]
c = 0 
for i in L:
    c = c+1 
print(c)

#Q Sum of elements in the list 
L = [1,2,3,4,5,6,7,8,9,0] 
c=0
for i in L: 
    c = c+i
print(c)

#Q Average of elements in list 
L = [1,2,3,4,5,6,7,8,9,0]
s=0
c=0
for i in L:
    s=s+i
    c=c+1
print(s/c)

#Q Sum of square of each element in the list 
L = [1,2,3,4,5,6,7,8,9,0]
s=0
for i in L:
    s=s+i**2 
print(s)

#Q Count even and odd numbers in the list 
L = [1,2,3,4,5,6,7,8,9,0]
e=0
o=0
for i in L:
    if i%2 == 0:
        e=e+1
    else:
        o=o+1
print(e)
print(o)

#Q Sum of square of even numbers and sum of cube of odd numbers in the list
L = [1,2,3,4,5,6,7,8,9,0]
e=0
o=0
for i in L:
    if i%2 == 0:
        e=e+i**2
    else: 
        o=o+i**3
print(e)
print(o)

#Q  Count  the number of vowels and consonents in the name 
name = input('enter name:')
v=0
c=0
for i in name:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        v=v+1
    else:
        c=c+1
print(v)
print(c)