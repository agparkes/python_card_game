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
        
        print(self.cards)
        
d = Deck()