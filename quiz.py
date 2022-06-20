print("Welcome to my quiz name")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("Is Python a programming langauge? True or False ")
if answer.lower() == "true":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("Can you build AI with Python? True or False ")
if answer.lower() == "true":
    print('correct!')
    score += 1
else:
    print('incorrect')

print("You got " + str(score) + " corect questions" )
print("You got " + str((score /5) *100) + " %" )