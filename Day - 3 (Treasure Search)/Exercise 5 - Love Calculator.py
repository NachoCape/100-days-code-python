# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
true = 0
love = 0
for i in range(len(name1)):
    if name1[i] == "t" or name1[i] == "r" or name1[i] == "u" or name1[i] == "e":
        true += 1
    if name1[i] == "l" or name1[i] == "o" or name1[i] == "v" or name1[i] == "e":
        love += 1

for j in range(len(name2)):
    if name2[j] == "t" or name2[j] == "r" or name2[j] == "u" or name2[j] == "e":
        true += 1
    if name2[j] == "l" or name2[j] == "o" or name2[j] == "v" or name2[j] == "e":
        love += 1
if true < 1 or true > 9:
    print(f"Your score is {true}{love}, you go together like coke and mentos.")
elif true == 4 or (true == 5 and love == 0):
    print(f"Your score is {true}{love}, you are alright together.")
else:
    print(f"Your score is {true}{love}.")
