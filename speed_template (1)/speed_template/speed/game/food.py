import random
import textwrap

class Food:
    def random_word(random):
        with open("wordlist.10000.txt", "rt") as file:
            string=file.read()
            quotes=string.splitlines()
            random_quotes=random.choice(quotes)

  
"""print("Welcome to the word game. Let's play!")
print(f"The word starts with: {random_quotes:.1}")
guess=input("Guess the word: ")
if guess== random_quotes:
    print("That's correct!")
else:
    print("Haha sucker. That's wrong.")"""
