# While loop and Control Statements

#Q  Print numbers from 1 to n using while loop
n = int(input('enter n: '))
i = 1

while i <= n:
    print(i)
    i += 1

#Q Sum of numbers from 1 to n using while loop
n = int(input('enter n: '))
i = 1
s = 0

while i <= n:
    s = s + i
    i += 1

print(s)

#Q  Print even numbers from 1 to n (using continue)
n = int(input('enter n: '))
i = 1

while i <= n:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

#Q Stop loop when number is divisible by 7 (using break)
i = 1

while True:
    if i % 7 == 0:
        print(i)
        break
    i += 1

#Q Simple menu-driven loop (exit using break)
while True:
    print("1. Say Hello")
    print("2. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("Hello")
    elif choice == 2:
        print("Exiting...")
        break
    else:
        print("Invalid choice")