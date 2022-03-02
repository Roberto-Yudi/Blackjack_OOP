import random


class Deck:

    def __init__(self):
        self.cards = []

    def generate(self):
        for x in range(2, 11):
            for y in range(4):
                self.cards.append(x)
        for x in ['A', 'J', 'Q', 'K']:
            for y in range(4):
                self.cards.append(x)

    def draw(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
