import random
class Deck:

    def __init__(self):
        self.cardDeck = self.generate_pack()

    #create a new pack of cards
    def generate_pack(self):
        cards = []
        suits = ["Heart", "Club", "Spade", "Diamond"]
        card_types = ["Ace","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for card in card_types:
                cards.append({'Suit': suit, 'Value': card})
        self.cardDeck = cards
        return cards

    def shuffle_deck(self):
        random.shuffle(self.cardDeck)

    #check if there are enough cards to draw a hand
    def check_remaining(self):
        if len(self.cardDeck) > 5:
            return True
        else:
            return False

    def deal_hand(self):
        hand = []
        count = 0
        while count < 5:
            #take card from top and remove it
            hand.append(self.cardDeck[-1])
            self.cardDeck.remove(self.cardDeck[-1])
            count+=1
        return hand
