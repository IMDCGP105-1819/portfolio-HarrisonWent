from Poker import Deck

Deck = Deck()
Deck.shuffle_deck()

def dealer():
    while 1==1:

        #check if there enough remaining card to make a hand
        while Deck.check_remaining():
            input("Enter key to deal hand")

            #deal hand from deck
            hand = Deck.deal_hand()
            for card in hand:
                #print card in hand
                print(card['Suit'], card['Value'])

        #Get new deck and shuffle
        print("Out of cards! ...Shuffling")
        Deck.generate_pack()
        Deck.shuffle_deck()

dealer()