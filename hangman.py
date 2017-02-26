import random,sys,os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
        
def welcome():
    print('\n')
    start = raw_input("Press enter/return to start or Q to quit: ").lower()
    if start == 'q':
        print("Bye!!")
        sys.exit()
    else:
        return True

        
def draw(wrong_guesses,right_guesses,secret_word):
    clear()
    print("Strikes {}/{}".format(len(wrong_guesses),strikes))
    print('\n')
    
    print("Bad guesses - "),
    for x in wrong_guesses:
        print(x),
    print('\n\n')
        
    for letter in secret_word:
        if letter in right_guesses:
            print(letter),
        else:
            print('_'),
    print('\n')
    
    
def get_guess(wrong_guesses,right_guesses):
    while True:
        guess_letter = raw_input("Guess a letter: ").upper()
        
        if len(guess_letter) != 1:
                print("You can guess only a single letter")
            
        elif guess_letter in right_guesses or guess_letter in wrong_guesses:
            print("You have already guessed that letter!")

        elif not guess_letter.isalpha():
            print("You can enter only letters")
            continue
        else:
            return guess_letter
        


def play(done):
    secret_word = random.choice(words).strip()
    right_guesses = []
    wrong_guesses = []
    strikes = 6
    
    while True:
        draw(wrong_guesses,right_guesses,secret_word)
        guess_letter = get_guess(wrong_guesses,right_guesses)
        
        if guess_letter in secret_word:
            right_guesses.append(guess_letter)
            found = True
            
            for letter in secret_word:
                if letter not in right_guesses:
                    found = False
            if found:
                print('\n')
                print("You Win!!")
                print("The secret word is - {}".format(secret_word))
                done = True
        else:
            wrong_guesses.append(guess_letter)
            if len(wrong_guesses) == strikes:
                draw(wrong_guesses,right_guesses,secret_word)
                print("You lost :-(")
                print("The secret word is - {}".format(secret_word))
                done = True
                
        if done:
            print('\n')
            play_again = raw_input("Play again? Y/n: ").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()
                    
        
                
words = []
with open('sowpods.txt','r') as f:
    words = list(f)
    
done = False
strikes = 6
while True:
    clear()
    print("<--- Welcome to Hangman Game --->")
    welcome()
    print('\n')
    play(done)
    

