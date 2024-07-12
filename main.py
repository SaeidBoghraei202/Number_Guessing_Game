import random

no = random.randint(1, 5)

while True:

    guess = input('What number do you guess ?')

    if guess.isdigit():

        guess = int(guess)
    else:
        print('Number is not valid')
        continue

    if guess == no:
        print('That\s Correct')
        quit()

    if guess == 0:
        print('The program was closed')
        break
    else:
        print('Wrong Number')
