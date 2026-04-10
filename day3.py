# IF ELSE Conditions, Multiple conditions , Nested Queries

#Q Grade the marks 
m = int(input('enter marks'))

if m>90 and m<=100:
    print('A')
elif m>70 and m<=90:
    print('B')
elif m>50 and m<=70:
    print('C')
elif m>30 and m<=50:
    print('D')
else:
    print('E')

#Q Take salary as input and put tax percent then calculate net salary.
sal = int(input('enter salary'))
if sal < 25000:
    print('net salary', sal - (sal*0)/100)
elif sal >= 25000 and sal < 50000: 
    print('net salary', sal - (sal*10)/100) 
elif sal >= 50000 and sal < 100000: 
    print('net salary', sal - (sal*30)/100) 
else: 
    print('net salary',sal - (sal*50)/100) 

#Q Check if no.is divisible by 5,7 both ,only by 5 ,only by 7 or by none of them 
n = int(input('enter n'))

if n%5 == 0:
    if n%7 == 0:
        print(n,'is divisible by both 5 and 7')
    else:
        print(n,'is divisible by 5 only')
elif n%7 == 0:
    print(n,'is divisible by 7 only')
    
else: 
    print(n,'is not divisible by any of them') 

#Q Check the weather conditions
w = input('enter weather')

if w == 'sunny':
    temp = int(input('enter temp'))
    if temp >= 30 and temp <= 50:
        print('play') 
    else: 
        print('not play') 
        
elif w == 'winter': 
    temp = int(input('enter temp'))
    if temp >= 10 and temp <= 20:
        print('play') 
    else:
        print('not play')
    
elif w == 'rainy':
      con = input('enter rainy con')
      if con == 'heavy':
          print('not play') 
      else:
          print('play')
else:
    print('Invalid') 

#Q Restaurent menu
print('Available Items are Pizza Burger')
order = input('place your order:').lower()
if order == 'pizza':
    top = input('select toppings veggies, corn, cheese')
    if top == 'veggies':
        print('your',top,order,'price is 150')
    elif top == 'corn':
        print('your',top,order,'price is 180')
    elif top == 'cheese':
        print('your',top,order,'price is 220')
    else:
        print(top,order,'is not available')
elif order == 'burger':
    category = input('select category veg, non veg')
    if category == 'veg':
        print('Your',category,order,'price is 60')
    else : 
        print('your',category,order,'price is 300')
else:
    print('Your order is not on the menu')
    