class Card():
    def __init__(self, value, suit, ):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck():

    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        print(self.cards)

Deck()

