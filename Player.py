
class Player:
    def __init__(self, playerName: str, playerLife, playerID): 
        self.playerName = playerName
        self.hand: list[str] = []
        self.playerLife = playerLife
        self.playerID = playerID
        self.cementery: list[str] = []

    def __str__(self):
        return self.playerName
    
    def show_hand(self):
        """Display the player's current hand"""
        print(f"{self.playerName}'s hand:")
        for i, card in enumerate(self.hand, 1):
            print(f"  {i}. {card}")
        print(f"Cards in hand: {len(self.hand)}")