import unittest
from card_game import Deck

class TestDeck(unittest.TestCase):
    def test_draw(self):
        deck = Deck()
        card = deck.draw()
        self.assertIsNotNone(card)

if __name__ == "__main__":
    unittest.main()