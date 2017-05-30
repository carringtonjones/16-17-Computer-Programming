# Add an import statement here so we can use the random.choice function.
import random

# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
vocab = {'uno' : 'one', 'dos': 'two','amarillo' : 'yellow', 'el tren' : 'train',
         'la salida' : 'exit', 'el billete' : 'ticket', 'mezcla' : 'mix',
         'las zanahorias' : 'carrots', 'las cebollas' : 'onions', 'las setas' : 'mushrooms',
         'los quisantes' : 'peas', 'la carne' : 'meat', 'los mariscos' : 'shellfish',
         'las fresas' : 'strawberries', 'los melocontones' : 'peaches', 'la mermelada' : 'jam',
         'la mentequilla' : 'butter', 'los tostadas' : 'toast', 'los huevos' : 'eggs', 'el arroz' : 'rice',
         'alto/a' : 'tall', 'aburrido/a' : 'boring', 'antipatico/a' : 'mean', 'simpatico/a' : 'nice',
         'bajo/a' : 'short'} 


# Start the game.
print("Let's play Flash Cards!")
right = 0


# Loop until the player gets 7 consecutive words correct.
while right < 25:
    # Create a list called spanish (or french) which contains the
    # keys from your vocab dict.
    spanish = list(vocab.keys())

    # Use the choice function to select a random word from the
    # list of keys. Store this word in a variable called question.
    question = random.choice(spanish)

    # Store the corresponding value for that key in a variable
    # called answer.
    answer = vocab[question]

    # Print the question word and prompt the user for a guess.
    guess = input('What is the translation of ' + question + ' in English')

    # If guess is equal to answer, print a message stating so and
    # increase the right total by 1. Otherwise, print a message
    # telling the player the correct answer and reset right to zero.
    if guess == answer:
        print('Good Job')
        right += 1
    else:
        print('Nope')
        right = 0 

    # Print the number of consecutive correct answers so far.
    print('Your streak is ' + str(right) + '.')


          
# End the game.
print("Good job. That's all of the correct answers in a row. You win!")
