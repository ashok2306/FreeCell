# Card class is used to create a Card object by passing the face value and the suit of the card.
# Symbols are generated based on the suit to enhance the output
# The class would also have methods to access the symbol, face, suit of the card


# Class Card to initialize the card object
class Card:
    # To create the Card object the card face and the card suit parameters are required.
    def __init__(self, cardFace, cardSuit):
        self.cardFace = cardFace
        self.cardSuit = cardSuit

        # Creates the character for the card based on the face value of the card.
        # 0 is the face value to create a blank card object. Assign A, X, J, Q, K when the face value is
        # 1, 10, 11, 12 ,13 respectively
        if self.cardFace == 0:
            self.character = 0
        elif self.cardFace == 1:
            self.character = 'A'
        elif self.cardFace == 10:
            self.character = 'X'
        elif self.cardFace == 11:
            self.character = 'J'
        elif self.cardFace == 12:
            self.character = 'Q'
        elif self.cardFace == 13:
            self.character = 'K'
        else:
            # If the character doesn't belong to anything of the above, use the card face as the character
            self.character = str(self.cardFace)

        # Generate symbol based on the card suit using unicode character
        if self.cardSuit == 0:
            self.symbol = 0
        elif self.cardSuit == 'H':
            self.symbol = u'\u2661'
        elif self.cardSuit == 'D':
            self.symbol = u'\u2662'
        elif self.cardSuit == 'C':
            self.symbol = u'\u2663'
        elif self.cardSuit == 'S':
            self.symbol = u'\u2660'
        else:
            self.symbol = self.cardSuit

    # Method to return the string by combining the character and symbol of the card seperated by colon
    def __repr__(self):
        return str(self.character) + ':' + str(self.symbol)

    # Method to return the face value of the card object
    def get_face(self):
        return self.cardFace

    # Method to return the suit of the card object
    def get_suit(self):
        return self.cardSuit

    # Methos to return the symbol of the card object
    def get_character(self):
        return self.character
