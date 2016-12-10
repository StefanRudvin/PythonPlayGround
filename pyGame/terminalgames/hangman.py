import random
import os

alphabet = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def gensecretword(word):
	global secretword
	secretword = word[random.randint(0, 64)]
	return secretword

def underscore(word):
	# word = secretword
	found = 0
	for i in word:
		##go through all the guessed letters and print as revealed if letter is found from guesslist
		for x in guessed:
			if x == i:
				found = 1
		if (found == 1):
			print(i +' ',end='')
			found = 0
		else:
			print('_ ',end='')

def playAgain():
   # This function returns True if the player wants to play again, otherwise it returns False.
   print('Do you want to play again? (yes or no)')
   return input().lower().startswith('y')

# Cycle through each letter in secretword.
#

def wordin():
	count = 0
	for i in secretword:
		if i in guessed:
			count += 1
	print(count)
	if count == len(secretword):
		return True

os.system('clear')

print("Welcome to hangman!")

while True:
	guesses = 0
	gameIsPlaying = True
	gensecretword(words)
	guessed = []
	while gameIsPlaying:
		while guesses < 10:
			print('Im thinking of a word this long: ')
			print(''), underscore(secretword)
			print('Turns left: ', 10 - guesses)
			print('Your guesses: ', str(guessed).strip('[').strip(']'))
			print('Enter your guess:')
			x = input()
			if x in alphabet:
				guessed.append(x)
				if x in secretword:
					if wordin():
						guesses = 20
						gameIsPlaying = False
						os.system('clear')
						print('Congratulations! You won the game! :)')

					else:
						os.system('clear')
						print('The letter was included in the word!')
				else:
					os.system('clear')
					print('Your guess was not in the word :(')
					guesses += 1
			else:
				os.system('clear')
				print('Invalid input!')
		if guesses == 10:
			print('Out of turns, you lose!')
			print('The word was: ' + secretword)
			gameIsPlaying = False
	if not playAgain():
		break
