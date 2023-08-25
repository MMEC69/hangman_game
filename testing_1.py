import random

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)
"""
print(someWords)

if "apple" in someWords:
    print("Apple is in list.")

if "woodapple" in someWords:
    print("Woodapple is in list")
else:
    print("Wooodapple is not in list")
"""

print(word)

print("Guess the word! HINT: word is a name of a fruit")

guesses = ""

while True:
    failed_times = 0
    for single_word in word:
        if single_word in guesses:
            print(single_word, end = " ")
        else:
            print("_", end = " ")
            failed_times +=1

    print()

    if failed_times == 0:
        print("Congrats!! you have found the word, \nThe word is {}".format(word))

    guessed_word = input("Enter the guess: ")

    guesses +=guessed_word

    if guessed_word not in word:
        print("Try again.")
        continue


