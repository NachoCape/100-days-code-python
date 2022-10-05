import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
list = [rock, paper, scissors]
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper \
or 2 for Scissors."))
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
random_number = random.randint(0, 2)
if choose >= 0 and choose <= 2:
    print(f"Computer chose:\n{list[random_number]}")
    if (choose == 0 and random_number == 2) or \
        (choose == 1 and random_number == 0) or \
            (choose == 2 and random_number == 1):
        print("You won")
    elif choose == random_number:
        print("It's a draw")
    else:
        print("You lose")
else:
    print("You typed an invalid number, you lose!")
