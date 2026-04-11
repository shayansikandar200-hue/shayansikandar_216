import random

class Deck:
    def __init__(self):
        self.cards = list(range(1, 14)) * 4
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class WarGame:
    def __init__(self):
        self.deck = Deck()
        self.score = {"Player": 0, "Computer": 0}

    def play(self):
        while len(self.deck.cards) >= 2:
            p = self.deck.draw()
            c = self.deck.draw()

            if p > c:
                self.score["Player"] += 1
            elif c > p:
                self.score["Computer"] += 1

        print("Final Score:", self.score)

if __name__ == "__main__":
    game = WarGame()
    game.play()