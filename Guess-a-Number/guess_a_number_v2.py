import random


def start_screen():
 

def play():
    
    print("Let's play a game!")
    print("I'm thinking of a number from 1 to 100")
    print("You try to guess, and I'll tell you if you're right.")

    num = random.randint(1, 100)

    got_it = False
    limit = 5
    tries = 0

    while got_it == False and tries < limit:
        
        guess = input("What number am I thinking of? ")
        guess = int(guess)
        
        if guess < num:
            print("Nope. Your guess is too low.")
        elif guess > num:
            print("Nope. Your guess is too high.")
        else:
            got_it = True

        tries += 1

    if got_it == True:
        print("You're a winner!")
    else:
        print("You r dum")


start_screen()

again = True

while again == True:
    play()

    answer = input("Would you like to play again? ")

    if answer == 'no':
        again = False

print("Game over")








