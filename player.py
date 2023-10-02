from hand import Hand
from chips import Chips
class Player:
    def __init__(self, chips): 
        self.chips = Chips(chips)
        self.hand = Hand()
        