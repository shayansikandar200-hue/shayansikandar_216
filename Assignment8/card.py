"""
Card class
"""

import unittest


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):

        return f"{self.rank} of {self.suit}"


class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card("Hearts", "A")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "A")

    def test_card_string(self):
        card = Card("Spades", "K")
        self.assertEqual(str(card), "K of Spades")


if __name__ == "__main__":
    unittest.main()