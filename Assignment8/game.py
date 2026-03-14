"""
Game class
Simple War card game.
"""

import unittest
from deck import Deck
from player import Player


class Game:
    """Simple card game"""

    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player1"), Player("Player2")]
        self.scores = {"Player1":0, "Player2":0}

    def deal_cards(self):
        self.deck.shuffle()
        while len(self.deck.cards) > 0:
            for player in self.players:
                card = self.deck.deal()
                if card:
                    player.add_card(card)

    def play_round(self):
        p1 = self.players[0].play_card()
        p2 = self.players[1].play_card()

        if not p1 or not p2:
            return

        if p1.rank > p2.rank:
            self.scores["Player1"] += 1
        elif p2.rank > p1.rank:
            self.scores["Player2"] += 1


class TestGame(unittest.TestCase):

    def test_game_setup(self):
        game = Game()
        self.assertEqual(len(game.players), 2)

    def test_deal_cards(self):
        game = Game()
        game.deal_cards()
        total_cards = len(game.players[0].hand) + len(game.players[1].hand)
        self.assertEqual(total_cards, 52)

    def test_scores_dictionary(self):
        game = Game()
        self.assertEqual(game.scores["Player1"], 0)


if __name__ == "__main__":
    unittest.main()