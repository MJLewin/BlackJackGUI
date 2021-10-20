"""
File: mlewincards.py
Author: Michael Lewin
Module for playing cards, with classes Card and Deck.
Updates cards.py from Kenneth Lambert.
Update tweaks classes to be more useful for a GUI Blackjack game.
"""

import random

class Card(object):
    """A card object with a value, suit, and rank."""
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('spades', 'diamonds', 'hearts', 'clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        self.value = str(rank) + suit[0]
        self.hidden = False
    
class Deck(object):
    """A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Removes and returns the top card or None
        if the deck is empty."""
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def __len__(self):
        """Returns the number of cards left in the deck."""
        return len(self.cards)

    def __str__(self):
        """Returns the string representation of a deck."""
        result = ''
        for c in self.cards:
            result = self.result + str(c) + '\n'
        return result

    

        
