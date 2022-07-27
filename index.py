"""
File: index.py
Updated by: Michael Lewin
Semester Summer 2021
Due: 08/19/2021
Instructor: Darin McCammon
This module defines a gui version of the blackjack class
and plays a game of blackjack with a dealer and a player.
"""

from mlewincards import Card, Deck
from mlewinblackjack import Player, Dealer
from breezypythongui import EasyFrame
from tkinter import PhotoImage

class GuiBlackjack(EasyFrame):
    """This class represents the GUI framework
    for a blackjack game."""

    def __init__(self):
        """Sets up the initial state of the blackjack game"""
        # Initializes game tracking statistics for Game Over button
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.gamesLost = 0
        self.blackJacks = 0
        # Instantiates deck, shuffles it, dealer and player start with 2 cards
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
        # One dealer card is face down to start
        self.dealer.cards[0].hidden = True
        # GUI elements
        EasyFrame.__init__(self, width = 800, height = 550,
                           title = "Blackjack")
        self.addLabel("Dealer Hand", 0, 0)
        self.addLabel("Player Hand", 3, 0)
        self.hitBtn = self.addButton("Hit", 5, 0,
                                     command = self.hit)
        self.standBtn = self.addButton("Stand", 5, 1,
                                       command = self.stand)
        self.restartBtn = self.addButton("Restart", 5, 3,
                                         command = self.restart)
        self.gameOverBtn = self.addButton("Game over", 5, 4,
                                          command = self.gameOver)
        self.updateImages()

    def updateImages(self):
        """Updates the images for the cards in player and dealer hands"""
        self.cardImages = []
        index = 0
        for card in self.dealer.cards:
            dealerCard = self.addLabel("", 1, index)
            image = PhotoImage(file = self.imageHelper(card))
            dealerCard["image"] = image
            self.cardImages.append(image)
            index += 1
        index = 0
        for card in self.player.cards:
            playerCard = self.addLabel("", 4, index)
            image = PhotoImage(file = self.imageHelper(card))
            playerCard["image"] = image
            self.cardImages.append(image)
            index += 1
        
    def imageHelper(self, card):
        """returns a string containing the related cards image"""
        folder = 'DECK/'
        ext = '.gif'
        file = ''
        if card.hidden == False:
            file = card.value
        else:
            file = 'b'
        return folder + file + ext

    def hit(self):
        """Gives player another card from the deck,
        updates images, checks for bust and ends round if so"""
        self.player.hit(self.deck)
        self.updateImages()
        points = self.player.getPoints()
        if points > 21:
            self.scoreGame()

    def stand(self):
        """Reveals dealer's hidden card, begins dealer's
        turn to play, updates images and ends round"""
        self.dealer.cards[0].hidden = False
        self.dealer.hit(self.deck)
        self.updateImages()
        self.scoreGame()

    def gameOver(self):
        """Disables buttons, pops up statistics about the game"""
        self.hitBtn['state'] = 'disabled'
        self.standBtn['state'] = 'disabled'
        self.restartBtn['state'] = 'disabled'
        self.gameOverBtn['state'] = 'disabled'
        self.messageBox(title = 'Statistics',
                    message = "Games Played: " + str(self.gamesPlayed) + "\n" +
                    "Games Won: " + str(self.gamesWon) + "\n" +
                    "Games Lost: " + str(self.gamesLost) + "\n" +
                    "Blackjacks: " + str(self.blackJacks))
        self.exit()

    def exit(self):
        self.destroy()

    def restart(self):
        """resets the game board to play another round"""
        self.results['text'] = ''
        self.hitBtn['state'] = 'normal'
        self.standBtn['state'] = 'normal'
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
        self.dealer.cards[0].hidden = True
        self.updateImages()

    def scoreGame(self):
        """scoring logic to determine who won. Updates relevant
        statistics for player"""
        self.gamesPlayed += 1
        self.hitBtn['state'] = 'disabled'
        self.standBtn['state'] = 'disabled'
        self.results = self.addLabel('', 2, 2)
        playerPoints = self.player.getPoints()
        if playerPoints > 21:
            self.results['text'] = "You bust and lose"
            self.gamesLost += 1
        else:
            dealerPoints = self.dealer.getPoints()
            if dealerPoints > 21:
                self.results['text'] = "Dealer busts and you win"
                self.gamesWon += 1
            elif dealerPoints > playerPoints:
                self.results['text'] = "Dealer wins"
                self.gamesLost += 1
            elif dealerPoints < playerPoints:
                self.results['text'] = "You win"
                self.gamesWon += 1
            elif dealerPoints == playerPoints:
                if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
                    self.results['text'] = "You win"
                    self.blackJacks += 1
                    self.gamesWon += 1
                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                    self.results['text'] = "Dealer wins"
                    self.blackJacks += 1
                    self.gamesLost += 1
                else:
                    self.results['text'] = "There is a tie"
    
def main():
    GuiBlackjack().mainloop()
    quit()

if __name__ == "__main__":
    main()
