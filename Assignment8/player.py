"""
Player class
Represents a player in the card game.
"""

import unittest


class Player:
    """Represents a game player"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self):
        if self.hand:
            return self.hand.pop()
        return None


class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")
        self.assertEqual(len(player.hand), 0)

    def test_add_card(self):
        player = Player("Bob")
        player.hand.append("TestCard")
        self.assertEqual(len(player.hand), 1)

    def test_play_card(self):
        player = Player("Tom")
        player.hand.append("Card")
        card = player.play_card()
        self.assertEqual(card, "Card")
        self.assertEqual(len(player.hand), 0)


if __name__ == "__main__":
    unittest.main()