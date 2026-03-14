"""
Deck class
Represents a deck of cards.
"""

import random
import unittest
from card import Card


class Deck:
    """Represents a deck of playing cards"""

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None


class TestDeck(unittest.TestCase):

    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deal_card(self):
        deck = Deck()
        card = deck.deal()
        self.assertIsNotNone(card)
        self.assertEqual(len(deck.cards), 51)

    def test_shuffle(self):
        deck = Deck()
        deck.shuffle()
        self.assertEqual(len(deck.cards), 52)


if __name__ == "__main__":
    unittest.main()