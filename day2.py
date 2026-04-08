# Operators

# Arithmetic Operator

#Q Adding value of a and b 
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The addition of', a, '+', b ,'=' , a+b)

#Q Substraction of a and b
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The substraction of',a ,'-', b, '=', a-b)

#Q Multiplication of a and b 
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The multiplication of',a,'*',b,'=',a*b)

#Q Division of a and b
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The division of',a,'/',b,'=',a/b)

# Double division of and b 
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The double division of',a,'//',b,'=',a//b)

# Modulus of and b 
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The modulus of', a, '%', b ,'=' , a%b)

# Exponential of a and b
a = int(input('enter value of a'))
b = int(input('enter value of b'))
print('The exponential of', a, '**', b ,'=' , a**b)

# Finding the area of rectangle 
l=int(input('enter the length'))
b=int(input('enter the breadth'))    
area = l*b
print('Area of rectangle',area)


# Compound Assignment 
a=10
a += 5 # a = a+5
print(a)

x=10
x -= 10 #x= x-10
print(x)

i=2
i **= 3 
print(i)


# Comparison Operator 
a=5
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)


# Logical Operator 
a=True
b=False 
c=True
d=False

print(a and b)
print(b and d)
print(a and c)

print(a or b)
print(b or d)
print(a or c)

print(not a)
print(not b)


# Identity Operator 
a=10.0
b=10
print(a is b)
print(id(a))
print(id(b))

k=257
t=257
print(k is t)


print(id(k)) 
print(id(t))


# Membership Operator
name ='natasha'
print('n' in name)
print('b' in name)
print('n' not in name)
print('N' not in name)
