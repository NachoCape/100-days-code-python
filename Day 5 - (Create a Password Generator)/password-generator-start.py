#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

sum = nr_letters + nr_numbers + nr_symbols
list = sum * [None]
count = 0
while count < nr_letters:
    aux = random.randint(0, sum-1)
    if list[aux] == None:
        list[aux] = (random.choice(letters))
        count += 1
    else:
        continue
count = 0
while count < nr_numbers:
    aux = random.randint(0, sum-1)
    if list[aux] == None:
        list[aux] = (random.choice(numbers))
        count += 1
    else:
        continue
count = 0
while count < nr_symbols:
    aux = random.randint(0, sum-1)
    if list[aux] == None:
        list[aux] = (random.choice(symbols))
        count += 1
    else:
        continue
for i in list:
    print(i, end="")