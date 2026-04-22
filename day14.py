# Lists (Basics)

#Q Create a list and print all elements
L = [10, 20, 30, 40, 50]
for i in L:
    print(i)

#Q Find the length of a list
L = [1, 2, 3, 4, 5]
print(len(L))

#Q Access first and last element of list
L = [5, 10, 15, 20]
print('first:', L[0])
print('last:', L[-1])

#Q Add an element to the list
L = [1, 2, 3]
L.append(4)
print(L)

#Q Remove an element from the list
L = [1, 2, 3, 4]
L.remove(3)
print(L)

#Q Check if an element exists in list
L = [10, 20, 30, 40]
if 20 in L:
    print('present')
else:
    print('not present')