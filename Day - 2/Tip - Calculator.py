#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print(f"Welcome to the tip calculator.")
bill = input("What was the total bill?")
tip = input("What percentage tip would you like to give?")
split = input("How many people to split the bill?")
bill_div_split = float(bill)/float(split)
print(f"Each person should pay: ${round(bill_div_split + (bill_div_split * float(tip)/100), 2)}")
