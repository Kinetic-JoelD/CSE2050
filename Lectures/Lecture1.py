# Pick a random number bw 1 and 100 
import random

solution = random.randint(1,100)
guess = int(input('Guess a number in less than 5 tries'))


# have the user guess a number

while guess != solution:

    if guess == solution:
        print('Good Job!')


    elif guess > solution:
        print('Guess is too high')
        guess = int(input('Try Again'))


    elif guess < solution:
        print('Guess is too low')
        guess = int(input('Try Again'))


# tell them if its too high or too low until they get it

print('You solved it!')

