"""
Words list is from "https://gist.github.com/deekayen/4148741"
"""

import random
import time

# import words to list
file_name = "word_list.txt"
with open(file_name) as f:
    word_list = f.read().splitlines()

# random choice word
word = random.choice(word_list)

# making log
alphabet_list = ""

# main of Hangman game
t = 0

print("\n\nYou have 20 chances to make answer!\n\n")
time.sleep(0.5)

print("After 5 sec, the game will start!")
time.sleep(5)

while t <= 19:
    correct = True
    print("")
    for i in word:
        if i in alphabet_list:
            print(i, end=" ")
        else:
            print("_", end=" ")
            correct = 0
    print("")

    if correct:
        print("Finish...!\n\nThe answer was \"%s\"" % word)
        break

    tt = 20 - t
    print("time left : %d" % tt)
    t += 1
    alphabet = input("choose alphabet : ")

    if alphabet not in alphabet_list:
        alphabet_list += alphabet

    if alphabet in word:
        print("Correct")
    else:
        print("Wrong")

    if tt == 1:
        print("\nF A I L U R E\n\nThe answer was \"%s\"" % word)
