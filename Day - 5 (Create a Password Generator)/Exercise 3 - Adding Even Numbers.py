#Write your code below this row 👇
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)

#Write your code below this row 👇

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)