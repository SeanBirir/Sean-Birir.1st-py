#I am creating a game in which I CREATE A SECRET WORD and the user guesses random words until he gets it right.
"so we use a while loop to keep looping until the user gets it correctly."

from ast import While
from platform import python_branch

Secret_word = "python"
guess = ""

while guess != Secret_word:
    guess = input(" Enter word: ")

print(" you win ")
print(" game over")

#we can add more pieces of information.

Secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != Secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input(" Enter word: ")
        guess_count += 1
    else:
        out_of_guesses = True    

if out_of_guesses:        
    print(" out of guesses, you lose !")
else:
    print("you win !")    

print(" game over")