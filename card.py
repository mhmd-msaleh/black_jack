class Card: 
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank 
        self.value = value
        pass

    def __str__(self): 
        return self.rank + ' of ' + self.suit