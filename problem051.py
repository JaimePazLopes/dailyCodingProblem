# Problem #50 [Easy]
# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input,
# write a function that shuffles a deck of cards represented as an array using only swaps.
#
# It should run in O(N) time.
#
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

import random


# getting a random between 1 and k
def random_number(k):
    return random.randint(1, k)


def shuffle_deck(deck):
    # for each card get a random number, and swap the actual card with the card in the random position
    for index in range(0, len(deck)):
        position = random_number(len(deck)) - 1
        deck[index], deck[position] = deck[position], deck[index]


# create an sequential array to represent the cards
def create_new_deck():
    return [i+1 for i in range(52)]


# do all the process and print for visualization
def create_and_shuffle():
    print("New Deck")
    cards = [i+1 for i in range(52)]
    print(cards)
    shuffle_deck(cards)
    print(cards)
    print()


for _ in range(20):
    create_and_shuffle()


# i dont know if i really understand this problem, but this is what i got. really fast and simples,
# 10 ~15 minutes even with me adding a lot of other unrelated stuff
