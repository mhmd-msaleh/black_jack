from player import Player
from deck import Deck
from hand import Hand

def take_bet(player):
    while True: 
        try: 
            bet = int(input('How many chips do you like to bet? \n'))
            player.chips.bet(bet)
            break
        except ValueError as e: 
            print(e)
        except: 
            print('Wrong input! Please provide integer')
            continue
    pass 

def hit(hand, deck): 
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    pass

def hit_or_stand(hand, deck, playing_state): 
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x.lower() == 'h':
            hit(hand,deck)  # hit() function defined above

        elif x.lower() == 's':
            print("Player stands. Dealer is playing.")
            return False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player_hand, dealer_hand): 
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer_hand.cards[1])  
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')
    print("Player's Hand =",player_hand.value)
    pass 

def show_all(player_hand, dealer_hand): 
    print("\nDealer's Hand:", *dealer_hand.cards, sep='\n ')
    print("Dealer's Hand =",dealer_hand.value)
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')
    print("Player's Hand =",player_hand.value)
    pass

def player_busts(player):
    """Player cards are more that 21"""
    print("Busts Player !")
    player.chips.lose_bet()
    pass

def player_wins(player):
    print("Player wins !")
    player.chips.win_bet()
    pass

def dealer_busts(player):
    """"""
    print("Player Wins! Dealer Busts")
    player.chips.win_bet()
    pass
    
def dealer_wins(player):
    print("Dealer Wins !")
    player.chips.lose_bet()
    pass
    
def push():
    print("Player and Dealer Tied")
    pass

def clear_hands(hands): 
    for hand in hands: 
        hand.clear()

def replay():
    """Asks the player if they want to play again
    
    Args: 
        None

    Returns: 
        True if the player input is 'Yes', False if 'No' 
    """

    replay_answer = input("Do you want to play agian ?\n Type (Yes/No)\n").lower()
    if replay_answer == 'yes':
        return True 
    elif replay_answer == 'no': 
        return False
    pass

def play(): 
    # Print an opening statement
    print('Welcome to Black Jack')
    # Create player and dealer
    while True: 
        try:
            player = Player(int(input('How many chips do you want? \n')))
            break
        except: 
            print('Please select an integer')
            continue
    dealer_hand = Hand()

    ## Start the Game
    while True:
        # Create & shuffle the deck, 
        deck = Deck()
        deck.shuffle()

        # deal two cards to each player
        for round in range(2): 
            player.hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        
        
        # Prompt the Player for their bet
        take_bet(player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player.hand, dealer_hand)

        playing = True
        while playing:  # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            playing = hit_or_stand(player.hand, deck, playing)
            # Show cards (but keep one dealer card hidden)
            show_some(player.hand, dealer_hand)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.hand.value > 21: 
                player_busts(player)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player.hand.value <= 21: 
            while dealer_hand.value <=17: 
                hit(dealer_hand, deck)
        
            # Show all cards
            show_all(player.hand, dealer_hand)
        
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player)

            elif dealer_hand.value > player.hand.value:
                dealer_wins(player)

            elif dealer_hand.value < player.hand.value:
                player_wins(player)

            else:
                push()
        
        # Inform Player of their chips total
        print("\nPlayer's total chips: ",player.chips.total)
        clear_hands([player.hand, dealer_hand]) 
        if player.chips.total == 0: 
            print('You lost all your chips !!')
            break
        # Ask to play again 
        if not replay(): 
            break

if __name__ == '__main__':
    play()
