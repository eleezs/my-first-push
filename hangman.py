import random

# hangman pics
def print_scaffold(turns, words):
    # prints the scaffold
	if(turns == 6):
            print("_________")
            print("|	 |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________")

	elif(turns == 5):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|")
				print("|")
				print("|")
				print("|________")
	elif(turns == 4):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	 |")
				print("|	 |")
				print("|")
				print("|________")
	elif(turns == 3):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|")
				print("|	 |")
				print("|")
				print("|________")
	elif(turns == 2):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|/")
				print("|	 |")
				print("|")
				print("|________")
	elif(turns == 1):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|/")
				print("|	 |")
				print("|	/ ")
				print("|________")
	elif(turns == 0):
				print("_________")
				print("|	 |")
				print("|	 O")
				print("|	\|/")
				print("|	 |")
				print("|	/ \ ")
				print("|________")
				print()
				print("The word was %s." %words)
				print()



# Intro
print()
print("THE HANGMAN")
name = input("What is your name? ")
print(name, "Welcome To the Hangman Game")
print()
print("let The Game Beginning")
print()


# Create a list of words
words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

# The system chooses a word at random
words = random.choice(words)

# Telling the player to pick a word
print("The computer has guessed a word..")
print("Now is time for you to guess the word letter by letter")

# Create an empty variable
guesses = ""

# Declaring number of turns
turns = 6

print_scaffold(turns, words)

# Loop function of the game
while turns > 0:
    # counts the number of time the use fails
    fails = 0

    # taking in the characters of the word one after the other
    # here it checks the word that has been picked, if the char
    # is present in guesses it prints else it show the dash line
    for char in words:
        # if char in word == char in guesses
        if char in guesses:
            print(char)
            #print("You Guess Correctly, Guess Another!")
        else:
            print("_")

            # increment if player guesses the wrong word
            fails += 1

        # if fails == 0, player wins the game
    if fails == 0:
        print("You Win")

        # this prints the correct word
        print("The word is ", words)
        break

    # the user inputs and it is saved in guesses
    guess = input("Guess a Character: ").lower()
    guesses += guess

    # just trying out
    if len(guess) > 1:
        print("Stop cheating! Enter one word at a time.")
    elif guess == "":
        print("Don't you want to play again? Enter a letter.")



    # check if char is in word
    if guess not in words:
        turns -= 1
        print_scaffold(turns, words)

        # print wrong if the char doesn't match
        print("Wrong Character, Try Again")

        # print turns left
        print("You have ", + turns, "turns Left")

        if turns == 0:

            print("You Loose! Damn You Dead!!!")



