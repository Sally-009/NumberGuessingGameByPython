import random

# Get Number
min = 1
max = 10
num = random.randint(min, max)

# Title
print("--- Number Guessing Game by python ---")
print("Range:", min, '-', max)

# Get answer
i = 1 #counter
while i <= 3:
    choice = int(input("Try " + str(i) + ": "))
    i += 1
    # Check answer
    if choice == num:
        print("You got it!! The answer is", num)
        print("GAME CLEAR!")
        break
    else:
        print("Oops! It is incorrect...")
        if i == 4:
            print("GAME OVER!")
            print("The answer was", num)

