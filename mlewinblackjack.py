"""
File: mlewinblackjack.py
Author: Michael Lewin
Module defines the Player and Dealer classes for a game of blackjack.
Updates blackjack.py from Kenneth Lambert.
Update tweaks classes to be more useful for a GUI Blackjack game.
"""

from mlewincards import Deck, Card

class Player(object):
    """This class represents a player in
    a blackjack game."""

    def __init__(self, cards):
        self.cards = cards

    def hit(self, deck):
        self.cards.append(deck.deal())

    def getPoints(self):
        """Returns the number of points in the hand."""
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        """Dealt 21 or not."""
        return len(self.cards) == 2 and self.getPoints() == 21

class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        Player.__init__(self, cards)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        while self.getPoints() < 17:
            self.cards.append(deck.deal())

