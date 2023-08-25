import random

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)

print(word)

print("Guess the word! HINT: word is a name of a fruit")

guesses = ""
chances = len(word) + 2
#5

while chances > 0:
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

    if chances == 0:
        print("You are out of chances.\nBetter try next time.")
        break

    guessed_word = input("Enter the guess: ")
    chances -=1
    if chances == 0:
        print("You are out of chances.\nBetter try next time.")
        break
    guesses +=guessed_word



    if guessed_word not in word:
        print("Try again.")
        continue


