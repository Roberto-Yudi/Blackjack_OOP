
class Player():
    def __init__(self, deck, dealer=False):
        self.deck = deck
        self.dealer = dealer
        self.hand = []
        self.credits = 100
        self.bet = 0

    def hit(self, times):
        for x in range(times):
            card = self.deck.draw()
            self.hand.append(card)

    def show_hand(self, hide=False):

        if self.dealer:
            if hide:
                print(f'Dealer Hand:{self.hand[0]},?')
            else:
                print(f'Dealer Hand:{self.hand}')
                print(f'Total:{self.total()}')
        else:
            print(f'Your Hand:{self.hand}')
            print(f'Total:{self.total()}')

    def total(self):
        total = 0
        for x in self.hand:
            if isinstance(x, int):
                total += x
            elif x in "JQK":
                total += 10
            else:
                if total < 11:
                    total += 11
                else:
                    total += 1
        return total
