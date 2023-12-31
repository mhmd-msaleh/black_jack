import random
from card import Card

class Deck: 
    def __init__(self): 
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
        self.deck = []
        for suit in suits: 
            for rank in ranks: 
                self.deck.append(
                    Card(suit, rank, values[rank])
                )

    def shuffle(self): 
        """Shuffling the deck card
        
        Args: 
            None
        
        Returns: 
            None
        """
        random.shuffle(self.deck)
    
    def deal(self): 
        """Deals the last card of the deck
        
        Args: 
            None
            
        Returns: 
            Last Card in the deck
        """
        return self.deck.pop()
   
