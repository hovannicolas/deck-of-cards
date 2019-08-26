class Card:
    def __init__(self, value, suit, ):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        print(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards."

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt")
        actual = min(num, count)
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)




