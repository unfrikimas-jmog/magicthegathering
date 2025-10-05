from Deck import Deck
from Player import Player

def main() -> None: 
    
# Create players
    player1 = Player("Alice", 20, 1)
    player2 = Player("Bob", 20, 2)
    players = [player1, player2]
    
    # Create game
    deck = Deck()
    deck.deal_starting_hands(players)
    
    # Show players' hands
    player1.show_hand()
    print()
    player2.show_hand()

if __name__ == "__main__":
    main()