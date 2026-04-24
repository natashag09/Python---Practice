# Functions (Basics)

#Q Create a function to print "Hello"
def greet():
    print("Hello")

greet()


#Q Create a function to add two numbers
def add(a, b):
    print(a + b)

add(5, 10)


#Q  Create a function to check even or odd
def check(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

check(7)


#Q Create a function to find sum of numbers from 1 to n
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    print(s)

sum_n(5)


#Q Create a function to find maximum of two numbers
def maximum(a, b):
    if a > b:
        print(a)
    else:
        print(b)

maximum(10, 20)

