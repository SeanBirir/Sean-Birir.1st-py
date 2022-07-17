"""I want to create a language where all vowels in a word turn into the letter "x",
using for loops it is possible to do that."""

def translate(word):
    translation = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            translation = translation + "x"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter word :")))    