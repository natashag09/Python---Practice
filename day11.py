# Control Statements (Break, continue)


#Q Print numbers from 1 to 5 and stop the loop when the number becomes 3 using break
for i in range(1,6):
    print(i)
    if i == 3:
        break 
    print(i)

#Q Use a while loop to print numbers from 1 to 10 and stop the loop when the number becomes 5 using break
x=1
while x <= 10:
    print(x)
    if x == 5:
        break
    x=x+1
print("This statement will print after the loop")

#Q Iterate through a list and calculate the sum of first 3 elements using break
list = [1,2,3,4,5,6] 
s=0
c=0
for num in list:
    print(num)
    s = s+num
    c = c+1
    if c == 3:
        break
print('sum is:', (s))

#Q Use a while loop to calculate sum of numbers and stop the loop when count reaches 3 using break
s=0
c=0
while c<6:
    s = s+c
    c = c+1
    if c == 3:
        break
print('sum is:', s) 

#Q Print numbers from 1 to 3 and skip printing the second time when the number is 2 using continue
for i in range(1,4):
    print(i)
    if i == 2:
        continue
    print(i)

#Q Calculate sum of numbers from n to 1 using while loop
n=5
num=0
if n == 0:
    print('hello')
else:
    while n>0:
        num = num+n
        n = n-1
    print(num)

#Q Print numbers from 1 to 7 but skip printing number 5 using continue in while loop
x=0
while x <= 7:
    x = x+1
    if x == 5:
        continue
    print(x)
print('This statement will print after the loop')

#Q Use while loop to calculate sum and skip a specific count using continue
s=0
c=0
while c < 6:
    s = s+c
    c = c+1
    if (c == 5):
        continue
    print('count is:', (c))
print('sum is:', (s))