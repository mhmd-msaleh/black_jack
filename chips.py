class Chips: 
    def __init__(self, total = 100): 
        self.total = total
        self.last_bet = 0
        pass

    def __str__(self): 
        return self.total

    def bet(self, bet): 
        if bet > self.total: 
            raise ValueError('Bet is more than total')
        elif bet == 0: 
            raise ValueError('You cannot bet 0 chips')
        else: 
            self.last_bet = bet
    
    def win_bet(self): 
        self.total += self.last_bet

    def lose_bet(self): 
        self.total -= self.last_bet