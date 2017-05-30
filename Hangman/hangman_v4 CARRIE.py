#hangman
#carrington j.
#october 20, 2016


import os
import random

def show_start_screen():
        print(" _    ___  ___  ___   ___  _    ___  _ _   _ _  ___  _ _  ___        __ __  ___  _ _ ")
        print("| |  | __>|_ _|/ __> | . \| |  | . || | | | | || . || \ |/  _>  ___ |  \  \| . || \ |")
        print("| |_ | _>  | | \__ \ |  _/| |_ |   |\   / |   ||   ||   || <_/\|___||     ||   ||   |")
        print("|___||___> |_| <___/ |_|  |___||_|_| |_|  |_|_||_|_||_\_|`____/     |_|_|_||_|_||_\_|")

def show_credits():    
        print(" ___   ___  __ __  ___   ___  _ _  ___  ___   _  _  _  _  _ ")
        print("/  _> | . ||  \  \| __> | . || | || __>| . \ | || || || || |")
        print("| <_/\|   ||     || _>  | | || ' || _> |   / |_/|_/|_/|_/|_/")
        print("'____/|_|_||_|_|_||___> '___'|__/ |___>|_\_\ <_><_><_><_><_>")


        print(" ____  _  _  _     ___   __   ____  ____  __  __ _   ___  ____  __   __ _      __   __   __ _  ____  ____ ")
        print("(  _ \( \/ )(_)   / __) / _\ (  _ \(  _ \(  )(  ( \ / __)(_  _)/  \ (  ( \   _(  ) /  \ (  ( \(  __)/ ___)")
        print(" ) _ ( )  /  _   ( (__ /    \ )   / )   / )( /    /( (_ \  )( (  O )/    /  / \) \(  O )/    / ) _) \___ \ ")
        print("(____/(__/  (_)   \___)\_/\_/(__\_)(__\_)(__)\_)__) \___/ (__) \__/ \_)__)  \____/ \__/ \_)__)(____)(____/")
                                                            
def display_board(solved, guesses, strikes):

    if strikes == 0:
        print("  ________")
        print("  |    |   ")
        print("  |       ")  
        print("  |       ")   
        print("  |       ")
        print("  |       ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")
        
        print(solved + " [" + guesses + "]")
     
    elif strikes == 1:
        print("  ________")
        print("  |    |   ")
        print("  |    o   ")  
        print("  |       ")   
        print("  |       ")
        print("  |        ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")
        
        print(solved + " [" + guesses + "]")
     
    elif strikes == 2:
        print("  ________")
        print("  |    |   ")
        print("  |    o   ")  
        print("  |    |  ")   
        print("  |    |")
        print("  |      ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")
        
        print(solved + " [" + guesses + "]")
        
    elif strikes == 3:
        print("  ________")
        print("  |    |   ")
        print("  |    o   ")  
        print("  |   /|  ")   
        print("  |    |  ")
        print("  |       ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")
        
        print(solved + " [" + guesses + "]")
        
    elif strikes == 4:
        print("  ________")
        print("  |    |   ")
        print("  |    o   ")  
        print("  |   /|\  ")   
        print("  |    |  ")
        print("  |       ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")
        
        print(solved + " [" + guesses + "]")
     
    elif strikes == 5:
        print("  ________")
        print("  |    |   ")
        print("  |    o   ")  
        print("  |   /|\  ")   
        print("  |    |")
        print("  |   /   ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")

        print(solved + " [" + guesses + "]")
     
    elif strikes == 6:
        print("  ________")
        print("  |    |   ")
        print("  |    o   ")  
        print("  |   /|\  ")   
        print("  |    |")
        print("  |   / \  ")
        print(" _|_")
        print("|   |______")
        print("|          |")
        print("|__________|")
        
        print(solved + " [" + guesses + "]")

def win_screen():
        print(" _ _  ___  _ _   _ _ _  _  _ _  _  _  _  _  _  _  _  _  _  _  _  _ ")
        print("| | || . || | | | | | || || \ || || || || || || || || || || || || |")
        print("\   /| | || ' | | | | || ||   ||_/|_/|_/|_/|_/|_/|_/|_/|_/|_/|_/|_/")
        print(" |_| `___'`___' |__/_/ |_||_\_|<_><_><_><_><_><_><_><_><_><_><_><_>")
              
def lose_screen():
        print(" _ _  ___  _ _   _    ___  ___  ___  _  _  _  _  _ ")
        print("| | || . || | | | |  | . |/ __>| __>| || || || || |")
        print("\   /| | || ' | | |_ | | |\__ \| _> |_/|_/|_/|_/|_/")
        print(" |_| `___'`___' |___|`___'<___/|___><_><_><_><_><_>")

    
def get_category(path):
    files = os.listdir(path)

    print("SELECT A CATAGORY...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f
        
        with open(full_path, 'r') as file:
            print(str(i + 1) + ") " + file.readline().strip())

    choice = input("Enter what you've selected: ")
    choice = int(choice)

    return path + "/" + files[choice - 1]

def get_puzzle(file):

    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:])

def check(word, solved, guesses):
    
    for i in range(len(word)):
        if word[i].lower() in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        
        guess = input("Guess a letter: ")

        if len(str(guess)) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("I do not understand, please type one letter at a time.")

    
def play_again():

    while True:
        print()
        answer = input("Would you like to play again?")

        if answer.lower() == 'no' or answer.lower() == 'n':
            return False   
        elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        print("I do not understand :( sorry, please type yes or no.")


def play():

    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)

    right = ""
    wrong = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, right)
    display_board(solved, wrong, strikes) 

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter.lower() not in word.lower():
            strikes += 1
            wrong += (letter + ", ")
        else:    
            right += letter

        solved = check(word, solved, right)
        display_board(solved, wrong, strikes)


    if word == solved:
        win_screen()
    else:
        lose_screen()


def main():
    show_start_screen()

    playing = True

    while playing == True:       
        play()
        playing = play_again()
    
    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
    
