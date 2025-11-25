from random import randint
class DeckOfCards:
    original_deck = None
    current_players = 0

    def __init__(self, deck: list) -> None:
        if type(deck) != list:
            raise Exception("'deck' argument must be a list.")
        
        self.deck = deck
        DeckOfCards.original_deck = deck.copy()
        self.players = {}
     
    def add_players(self, num_players: int) -> None:
        for x in range(DeckOfCards.current_players + 1, DeckOfCards.current_players + num_players + 1):
            DeckOfCards.current_players += 1
            self.players[f"Player {x}"] = []

    # num_of_players can be an int or list
    # int will remove that many players
    # list will remove a specific set of players
    def remove_players(self, num_of_players: int | list) -> dict:
        if type(num_of_players) == int:
            for x in range(0, num_of_players):
                self.players.popitem()

        if type(num_of_players) ==  list:
            for player_num in num_of_players:
                self.players.pop(f"Player {player_num}")

        return self.players
    
    # Fisher–Yates shuffle
    # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Python_implementation:~:text=H%20B%20F.-,Python%20implementation,-%5Bedit%5D
    def shuffle(self) -> None:
        for i in range(len(self.deck) - 1, 0, -1):
            j = randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
    
    def deal(self, cards_per_player: int) -> None:
        if DeckOfCards.current_players == 0:
            raise Exception(f"There are {DeckOfCards.current_players} players to deal cards to.")

        if DeckOfCards.current_players * cards_per_player > len(self.deck):
            raise Exception(f"Not enough cards for {DeckOfCards.current_players} players.")
 
        # Assigns each key a card once, then repeats for cards_per_player  
        for x in range(cards_per_player):
            for player in self.players:
                self.players[player].append(self.deck[0])
                self.deck.pop(0)

    def draw(self, player_num: int, num_cards_to_draw: int = 1) -> None:
        if DeckOfCards.current_players == 0:
            raise Exception(f"There are {DeckOfCards.current_players} players to draw cards.")
        
        for x in range(0, num_cards_to_draw):
            key = f"Player {player_num}"
            self.players[key].append(self.deck[0])
            self.deck.pop(0)    
    
    def reset(self) -> None:
        self.deck = DeckOfCards.original_deck

    def cards_left(self) -> int:
        for cards_left, card in enumerate(range(0, len(self.deck) + 1)):
            continue
        
        return cards_left

    def change_deck(self, new_deck: list) -> None:
        if type(new_deck) != list:
            raise Exception("change_deck() takes a list argument only.")
        else:
            DeckOfCards.original_deck = new_deck.copy()
            self.deck = new_deck
            


cards = DeckOfCards(["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", 
    "S10", "SJ", "SQ", "SK", "HA", "H2", "H3", "H4", "H5", "H6", 
    "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "DA", "D2", "D3", 
    "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", 
    "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", 
    "CJ", "CQ", "CK"])
