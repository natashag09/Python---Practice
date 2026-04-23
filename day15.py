# Lists (Problem Solving)

#Q  Find sum of all elements in a list
L = [1, 2, 3, 4, 5]
s = 0
for i in L:
    s = s + i
print(s)


#Q Find maximum element in a list
L = [10, 25, 5, 40, 15]
m = L[0]
for i in L:
    if i > m:
        m = i
print(m)


#Q Count even and odd numbers in a list
L = [1, 2, 3, 4, 5, 6]
e = 0
o = 0
for i in L:
    if i % 2 == 0:
        e = e + 1
    else:
        o = o + 1
print('even:', e)
print('odd:', o)


#Q Find second largest element in a list
L = [10, 20, 30, 40, 50]
L.sort()
print(L[-2])


#Q Reverse a list 
L = [1, 2, 3, 4, 5]
print(L[::-1])


#Q Check if element exists in list
L = [5, 10, 15, 20]
x = int(input('enter number: '))
if x in L:
    print('present')
else:
    print('not present')
    