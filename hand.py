from card import Card

class Hand: 
    def __init__(self): 
        self.cards = []
        self.value = 0
        self.aces = 0
        pass

    def add_card(self, card): 
        # add card to cards 
        self.cards.append(card)
        # calculate value
        self.value += card.value
        # if there is an ace increment aces
        if card.rank == 'Ace': 
            self.aces += 1
        pass

    def adjust_for_ace(self): 
        """Treat aces as 1 if the hand value > 21
        """
        while self.value > 21 and self.aces: 
            self.value -= 10    # Ace value now is 1 
            self.aces -= 1      # Decrement #aces
        pass

    def clear(self): 
        self.cards.clear()
        self.value = 0 
        self.aces = 0 