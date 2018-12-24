# Problem Set 2, hangman.py
# Name: Viktor Karpilov
# Collaborators: -
# Time spent: i don`t know , but not too much (3-4 hours)

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def is_word_guessed(secret_word,letters_guessed):
    letters_guessed = set(letters_guessed)
    secret_word = set(secret_word)
    if(secret_word==letters_guessed&secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word,letters_guessed):
    result = ""
    for i in secret_word:
        if i in letters_guessed:
            result +=  i
        else:
            result += " _ "

    return  result

def get_avalible_letters(letters_guessed):
    alfavit = set('abcdefghijklmnopqrstuvwxyz')
    result = list(alfavit-set(letters_guessed))
    result.sort()
    return result


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    alfavit = set('abcdefghijklmnopqrstuvwxyz')

    # lives = int(input("Enter difficult"))
    warning = 3
    lives =6
    #print(secret_word)
    letters_guessed = []
    # print(get_avalible_letters(letters_guessed))
    def list_to_string(list):
        result = ""
        for i in list:
            result+= i
        return result


    while lives != 0 and not is_word_guessed(secret_word,letters_guessed):
        print("You have :",lives," lives")
        print("word :" + get_guessed_word(secret_word, letters_guessed))
        print("Avalible letters :"+list_to_string(get_avalible_letters(letters_guessed)))
        letter = input("Input pleas a letter :")
        if len(letter)!=1 :
            warning -= 1
            print("You entered something strange. You have ", warning, "warnings left")
        elif letter == "*" and with_hints:
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        elif letter in letters_guessed:
            warning -= 1
            print("You have entered this simbol before. You have ", warning, "warnings left")
        elif letter in secret_word :
            print("You god damn right !")
            letters_guessed.append(letter)
        elif not letter in alfavit and warning>0:
            warning -= 1
            print("You entered something strange. You have ",warning,"warnings left")

        else:
            print("Sorry , but no")
            if letter in set(["a","e","i","o","u"]):
                lives -= 1
            letters_guessed.append(letter)
            lives -= 1
        print("________________________")


    if(lives == 0):
        print(secret_word)
        print("You lose !")
    else:
        print(secret_word)
        print("Congratulaion , you have :",str(lives*len(set(secret_word)))," scores")

    pass



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ","")
    letters_set = set(my_word)
    if len(other_word) != len(my_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != other_word[i] and my_word[i] != "_":
            return False
        elif my_word[i] == '_' and other_word[i] != '_' and other_word[i] in letters_set:
            return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    result = "Posible words : "
    for i in wordlist:
        if match_with_gaps(my_word,i):
            result += i + " "
    if len(result) == len("Posible words : "):
        return "No matches found"
    return result



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global with_hints
    with_hints = True
    print("Game with hints")
    hangman(secret_word)
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

with_hints = False
if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
