1. This is a simple exercise, making use of object oriented programming in python.
2. Two classes are created, Card and Deck. 

3. The Card class:
    a. The Card class has two attributes, suit and value(single string characters)
    b. There is a __repr__ method that display the card's suit and value
    
3. The Deck class, is the work horse of the exercise:
    a. The Deck class has several instance methods such has a card attribute with all possible instances of the cards in the deck, private instance called _deal that accepts a number and removes that much from the deck, but not more than what is in the deck and so on.
    b. Custom ValueError messages are included to handle respective errors based on the exercise.
    c. Import from random shuffle, for the instance method called shuffle to shuffle a full deck.
    d. Instance method called deal_card uses the _deal method to deal a single card
    e. The deal_hand instance method accepts a number and uses the _deal method to deal a list of cards from the deck