import random

class Blackjack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        self.player_hand = []
        self.dealer_hand = []

    def draw_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def initial_deal(self):
        for _ in range(2):
            self.player_hand.append(self.draw_card())
            self.dealer_hand.append(self.draw_card())

    def hand_value(self, hand):
        value = sum(hand)
        if value > 21 and 11 in hand:
            hand[hand.index(11)] = 1
            value = sum(hand)
        return value

    def play(self):
        self.initial_deal()
        while True:
            print(f"Player hand: {self.player_hand}, value: {self.hand_value(self.player_hand)}")
            if self.hand_value(self.player_hand) > 21:
                print("Player busts! Dealer wins.")
                break
            move = input("Hit or Stand? ").lower()
            if move == "hit":
                self.player_hand.append(self.draw_card())
            elif move == "stand":
                break

        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw_card())

        print(f"Dealer hand: {self.dealer_hand}, value: {self.hand_value(self.dealer_hand)}")
        if self.hand_value(self.dealer_hand) > 21:
            print("Dealer busts! Player wins.")
        elif self.hand_value(self.dealer_hand) >= self.hand_value(self.player_hand):
            print("Dealer wins.")
        else:
            print("Player wins.")

game = Blackjack()
game.play()
