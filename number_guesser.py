import random 

top_of_range = input("Type a number " )

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("PLease type number larger than 0 next time")
        quit()
else:
    print("PLease type number next time")
    quit()

r = random.randint(0, top_of_range)
print(r)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Please type a number ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == r:
        print('You got it')
        break
    elif user_guess > r:
            print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")