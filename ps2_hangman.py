#!/usr/bin/python
# 6.00 Problem Set 3
# 
# Hangman
#
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

################################################ your code begins here!

secret_word = choose_word(wordlist); print secret_word
#secret_word = "apple"
secret_word_list = list(set(secret_word))

print "welcome to hangman!"
print "the secret_word is %d letters long. start guessing!" % len(secret_word)

show_hangman = list(len(secret_word) * " ") # make a list of spaces to use for the display

letters_guessed = [] #track incorrect guesses here
letters_removed = [] #track correct guesses here


while len(secret_word_list) > 0:
    guess = raw_input("enter a letter: ")        
    
    # case 1: the letter is in the word
    if guess in secret_word_list:
        print "found %s in the secret word %d times" % (guess, secret_word.count(guess))
        
        # something cute to display where in the word we found the correct guess
        letter_location = [] #store index of found letter for display purposes
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                letter_location.append(i)
        for i in letter_location:
            show_hangman[i] = guess
        print (" ").join(show_hangman)

        # remove the correct guess from the list, and track our correct guess
        secret_word_list.remove(guess)  
        letters_removed.append(guess)         

    # case 2: we guessed that letter correctly previously
    elif guess in letters_removed:
        print "already removed letter!"
    
    # case 3: we guessed that letter incorrectly previously
    elif guess in letters_guessed:
        print "already guessed that letter!"

    else:
        print "not found, guess again!"
        letters_guessed.append(guess)


print "YOU WIN!!! the secret word was '%s'" % secret_word

