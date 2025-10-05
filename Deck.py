import random 

class Deck: 
    def __init__(self):
        self.cards = []
        with open(r"c:\Users\josem\Downloads\the-ur-dragon--20250528-200136.txt") as deckList:
            for cards in deckList:
                self.cards.append(cards.strip())

    def shuffle_deck(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
        print("Deck shuffled!")

    def draw_card(self, player):
        """Player draws one card from deck"""
        if self.cards:
            card = self.cards.pop()
            player.hand.append(card)
            print(f"{player.playerName} drew a card: {card}")
        else:
            print("Deck is empty!")

    def Millcard(self, player):
        """Player mills one card from deck"""
        if self.cards:
            card = self.cards.pop()
            player.cementery.append(card)
            print(f"{player.playerName} mill a card: {card}")

    def scryCard(self, player):
        if self.cards: 
            card = self.cards.pop()
            print(f"{player.playerName} scry one: {card}")
            self.cards.append(card)


    def deal_hand(self, player, cards_to_deal=7):
        """Deal a specified number of cards to a player (default 7 for Magic)"""
        if len(self.cards) < cards_to_deal:
            print(f"Not enough cards in deck! Only {len(self.cards)} cards remaining.")
            cards_to_deal = len(self.cards)
            
        for _ in range(cards_to_deal):
            if self.cards:  # Check if deck still has cards
                card = self.cards.pop()  # Remove card from deck
                player.hand.append(card)  # Add to player's hand
        
        print(f"Dealt {cards_to_deal} cards to {player.playerName}")
        
    def deal_starting_hands(self, players, hand_size=7):
        """Deal starting hands to all players"""
        for player in players:
            self.deal_hand(player, hand_size)