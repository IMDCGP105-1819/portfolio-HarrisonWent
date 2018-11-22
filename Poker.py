class Deck:

    def generate_pack(self):

        cards = [{'Value' : "", 'Suit' : "", 'Position' : ""}]

        for a in range(1,14):
            if a == 1:

            elif a == 11:

            elif a == 12:

            elif a == 13:

            else:
                dict = {'value' : a, 'suit' : "Hearts", 'Position' : ""}
                cards.append(dict)

                dict = {'value': a, 'suit': "Clubs", 'Position': ""}
                cards.append(dict)

                dict = {'value': a, 'suit': "Spades", 'Position': ""}
                cards.append(dict)

                dict = {'value': a, 'suit': "Diamonds", 'Position': ""}
                cards.append(dict)


