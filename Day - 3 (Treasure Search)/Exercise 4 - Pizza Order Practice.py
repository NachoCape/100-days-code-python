# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sum = 0
if size == "S":
    sum += 15
    if add_pepperoni == "Y":
        sum += 2
elif size == "M":
    sum += 20
elif size == "L":
    sum += 25
if add_pepperoni == "Y" and size != "S":
    sum += 3
if extra_cheese == "Y":
    sum += 1
print(f"Your final bill is: ${sum}.")
