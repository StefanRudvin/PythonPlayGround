import random

guesses = 0

print('Hello! What is your name?')

name = input()

number = random.randint(1,20)

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guesses < 6:
	final = 6 - guesses
	final = str(final)
	print('Guesses left: ' + final)
	print('Take a guess: ')
	guess = input()
	guess = int(guess)
	guesses = guesses + 1
	if guess == number:
		break
	if guess < number:
		print('Your guess was too small')
	if guess > number:
		print('Your guess was too big!')

if guess == number:
	guesses = str(guesses)
	print('Congratulations! You found the right number with '+ final + ' guesses left!')

if guess != number:
	number = str(number)
	print('You lost! The number I was thinking of was ' + number)
