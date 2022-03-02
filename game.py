from player import Player
from deck import Deck
import time


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(self.deck)
        self.dealer = Player(self.deck, dealer=True)

    def play(self):
        print(f'You have {self.player.credits} points')

        self.player.hit(2)
        self.dealer.hit(2)

        while True:
            try:
                self.player.bet = int(input("Place your bet\n"))
                if self.player.bet <= 0:
                    print('You can\'t bet nothing.🙃')
                elif self.player.bet > self.player.credits:
                    print('You don\'t have enough credits.😐')
                else:
                    break
            except ValueError:
                print('Invalid input.🚫')

        self.dealer.show_hand(hide=True)
        time.sleep(2)
        self.player.show_hand()

        # BlackJack
        if self.player.total() == 21:
            if self.dealer.total() == 21:
                print(f'Dealer Hand:{self.dealer.hand}')
                print('BlackJack Tie!🤯')
                return
            print('---- ♠BlackJack!, You Win!🍀 ----')
            print(f'You earned: {self.player.bet * 1.5}')
            self.player.credits += self.player.bet * 1.5

            return

        # Player_hit_cycle

        while True:
            next_move = input('🤔\n1: Hit\n2: Stay\n')
            if next_move == '1':
                self.player.hit(1)

                self.player.show_hand()

                # Bust Check
                if self.player.total() > 21:
                    print('----You Busted!, Dealer wins.😒 ----')
                    self.player.credits -= self.player.bet
                    return
            elif next_move == '2':
                break
            else:
                print('Invalid Input.🚫')

        self.dealer.show_hand()

        # Dealer Hit Cycle

        while self.dealer.total() < 17:
            self.dealer.hit(1)
            print('Dealer Hit!')
            self.dealer.show_hand()
            time.sleep(2)

            # Bust Check
            if self.dealer.total() > 21:
                print('----Dealer Busted, You Win!😂 ----')
                print(f'You earned: {self.player.bet}')
                self.player.credits += self.player.bet

                return
        # Final Check

        if self.player.total() > self.dealer.total():
            time.sleep(2)
            print('----You have the best hand!, You Win.😁 ----')
            print(f'You earned: {self.player.bet}')
            self.player.credits += self.player.bet

            return
        elif self.player.total() == self.dealer.total():
            time.sleep(2)
            print('----It\'s a Tie!🤷----')
            return
        else:
            time.sleep(2)
            print('----Dealer have the best hand, Dealer Wins.😥 ----')
            self.player.credits += self.player.bet
            return


a = Game()
a.play()
