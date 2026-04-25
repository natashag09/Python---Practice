# Functions (Light Practice)

#Q Create a function that returns square of a number
def square(n):
    return n * n

print(square(5))


#Q  Create a function that returns the length of a string
def length(s):
    return len(s)

print(length("python"))


#Q Create a function that returns the larger of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 20))