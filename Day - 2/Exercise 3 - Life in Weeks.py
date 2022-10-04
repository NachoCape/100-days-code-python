# Create a program using maths and f-Strings that tells us how many days,

# weeks, months we have left if we live until 90 years old
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
res = 90 - int(age)
print(f"You have {res * 365} days, {res * 52} weeks, and {res * 12} months left.")

