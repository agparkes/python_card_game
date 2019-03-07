from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit  = suit
        
    def __repr__(self):
#        return "{} of {}".format(self.value, self.suit) #format less than python 3.6
        return f"{self.value} of shield {self.suit}" 

class Deck:
    def __init__(self):
        suits      = ["Lion", "Bear", "Wolf", "Gorilla"]
        values     = ["Emerald", "Diamond", "Ruby", "Sapphire", "Star", "Moon", "Fire", "Wind", "Earth", "Thunder", "Lightling", "Safe"]
        self.cards = [Card(value, suit) for suit in suits for value in values] 
        
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError ("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
        print(f"Going to remove {actual} cards")
        
    def deal_card(self):
        return self._deal(1)[0] 

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle_deck(self):
        if self.count() < 48:
            raise ValueError("Only full deck can be shuffled")
        shuffle(self.cards)
        return self #best practice to return self, a conventional thing to do
        
d = Deck()
d.shuffle_deck()
print(d._deal(3))
print(f"There are {d.count()} cards remaining")
#print(d._deal(48))
#d.shuffle_deck()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)
print(d.cards)