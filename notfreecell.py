# Importing Deck class from deck
from deck import Deck


# Class NotFreecell would have methods to implement the game rules for Free Cell
class NotFreecell:
    # Init method to initialize the game by calling the Deck class
    def __init__(self, value_start, value_end, number_of_suits):
        self.gameDeck = Deck(value_start, value_end, number_of_suits)

    # Method to return the string
    def __str__(self):
        return str(self.gameDeck)

    # Method to check if the game is over
    def isGameOver(self):
        self.gameDeck.check_game()

    # Method to call the drawCard class in the deck
    def draw(self, place, position):
        return self.gameDeck.drawCard(place, position)

    # Method to move the card by checking the Free cell rules
    def moveCard(self, fromPlace, toPlace, fromPos, toPos):

        # Converting fromPlace values to the actual position
        if fromPlace == '1':
            fromPlace = 'cascade'
        elif fromPlace == '2':
            fromPlace = 'cell'
        elif fromPlace == '3':
            fromPlace = 'foundation'

        # Converting toPlace values to the actual position
        if toPlace == '1':
            toPlace = 'cascade'
        elif toPlace == '2':
            toPlace = 'cell'
        elif toPlace == '3':
            toPlace = 'foundation'

        # Getting the card values of the source from the position mentioned
        fromCard, fromSuit = self.gameDeck.drawCard(fromPlace, int(fromPos) - 1)

        # Getting the card values of the destination from the position mentioned
        toCard, toSuit = self.gameDeck.drawCard(toPlace, int(toPos) - 1)

        # Checking the fromPlace
        if fromPlace == 'cascade':
            # If no card is present at the cascade
            if fromCard == 0:
                print(">> No card at this position to draw <<")

            elif toPlace == 'cascade':
                # If cascade is empty add the card at the position without any check
                if toCard == 0:
                    self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)

                else:
                    # If the cascade is already having a card then check the suit
                    if fromSuit == 'S' or fromSuit == 'C':
                        # Checking if the card is of opposite color
                        if toSuit == 'H' or toSuit == 'D':
                            # Checking if the toCard is one value less then the existing card
                            if int(fromCard) + 1 == int(toCard):
                                self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                            else:
                                print(">> Card cannot be moved to the position <<")

                        else:
                            print(">> Card cannot be moved to the position <<")

                    if fromSuit == 'H' or fromSuit == 'D':
                        # Checking if the card is of opposite color
                        if toSuit == 'S' or toSuit == 'C':
                            # Checking if the toCard is one less than the existing card
                            if int(fromCard) + 1 == int(toCard):
                                self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                            else:
                                print(">> Card cannot be moved to the position <<")

                        else:
                            print(">> Card cannot be moved to the position <<")

            elif toPlace == 'cell':
                # Checking if the cell is empty. If empty then move the card
                if toCard == 0:
                    self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                else:
                    # If the cell is not empty
                    print(">> Cell position entered is not empty <<")

            elif toPlace == 'foundation':
                # Checking if the foundation is empty
                if toCard == 0:
                    # Checking if the card is having value as 1 (Ace)
                    if fromCard == 1:
                        self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                    else:
                        # If the value is not Ace then card cannot be inserted
                        print(">> First card on a Foundation can only be an Ace <<")

                else:
                    # If the foundation is not empty then checking if the cards are of same suit
                    if fromSuit == toSuit:
                        # Checking if the fromCard is exactly one more than the existing card
                        if fromCard == toCard + 1:
                            self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                        else:
                            print(">> Card cannot be moved to Foundation because of different face value <<")
                    else:
                        print(">> Card cannot be moved to Foundation because of difference in Suit <<")

        elif fromPlace == 'cell':
            # Checking if the cell is empty
            if fromCard == 0:
                print(">> No card at this position to draw <<")

            elif toPlace == 'cascade':
                # Checking if the cascade mentioned is empty. If so add the card at the position without any check
                if toCard == 0:
                    self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                else:
                    # If the cascade is not empty checking for suits
                    if fromSuit == 'S' or fromSuit == 'C':
                        # Checking if the card is of opposite suit
                        if toSuit == 'H' or toSuit == 'D':
                            # Checking if the toCard is one value less than the fromCard
                            if int(fromCard) + 1 == int(toCard):
                                self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                            else:
                                print(">> Card cannot be moved to the position <<")

                        else:
                            print(">> Card cannot be moved to the position <<")
                    # Checking the suits
                    if fromSuit == 'H' or fromSuit == 'D':
                        # Checking if the card is of opposite suit
                        if toSuit == 'S' or toSuit == 'C':
                            # Checking if the toCard is one value less than the fromCard
                            if int(fromCard) + 1 == int(toCard):
                                self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                            else:
                                print(">> Card cannot be moved to the position <<")

                        else:
                            print(">> Card cannot be moved to the position <<")
            elif toPlace == 'cell':
                # Checking if the cell is empty. If empty then move the card
                if toCard == 0:
                    self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                else:
                    print(">> Cell position entered is not empty <<")

            elif toPlace == 'foundation':
                # Checking if the foundation at position is empty.
                if toCard == 0:
                    # If the foundation is empty then check if the value of the card is 1 (Ace)
                    if fromCard == 1:
                        self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                    else:
                        print(">> First card on a Foundation can only be an Ace <<")

                else:
                    # If the foundation is not empty check if the cards are from the same suit
                    if fromSuit == toSuit:
                        # Checking the value of the toCard if it is exactly one more then the fromCard
                        if fromCard == toCard + 1:
                            self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                        else:
                            print(">> Card cannot be moved to Foundation because of different face value <<")
                    else:
                        print(">> Card cannot be moved to Foundation because of difference in Suit <<")

        elif fromPlace == 'foundation':
            # If the foundation is empty
            if fromCard == 0:
                print(">> No card at this position to draw <<")
            elif toPlace == 'cascade':
                # Checking if the cascade at position is empty. If so then insert without any check
                if toCard == 0:
                    self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)

                else:
                    # If cascade is having a card then check the suit
                    if fromSuit == 'S' or fromSuit == 'C':
                        # Check if the toCard is of opposite suit
                        if toSuit == 'H' or toSuit == 'D':
                            # Check if the value of the toCard is one less than the fromCard
                            if int(fromCard) + 1 == int(toCard):
                                self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                            else:
                                print(">> Card cannot be moved to the position <<")

                        else:
                            print(">> Card cannot be moved to the position <<")

                    # Checking the card suit
                    if fromSuit == 'H' or fromSuit == 'D':
                        # Checking if the card is of different suit
                        if toSuit == 'S' or toSuit == 'C':
                            # Checking if the value of the toCard is ones less than the fromCard
                            if int(fromCard) + 1 == int(toCard):
                                self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                            else:
                                print(">> Card cannot be moved to the position <<")

                        else:
                            print(">> Card cannot be moved to the position <<")

            elif toPlace == 'cell':
                # Checking if the cell is empty. If so then insert the item
                if toCard == 0:
                    self.gameDeck.addCard(fromPlace, toPlace, int(fromPos) - 1, int(toPos) - 1)
                else:
                    # If the cell is not empty
                    print(">> Cell position entered is not empty <<")


def main():

    # Method to check if the value is between the start and end value
    def check_ip(start, end, value):
        # If value is between start and end then do nothing
        if end >= int(value) >= start:
            pass
        else:
            # If the value is not between start and end then display message and quit
            print("Invalid Input. Cannot continue with Game. Please start again")
            quit()


    # Calling the NotFreeCell class
    game = NotFreecell(1, 13, 4)

    option = 'm'

    # While loop until option is not m
    while option == 'm':
        # Checking if the game is over
        game.isGameOver()

        # Printing the game deck
        print(game)

        # Getting input from user
        option = input("m to Move. \nAny other key to Quit Game \nEnter your option: ")

        # Checking is option is not m
        if option != 'm':
            quit()

        # Getting user inputs for from Place, from Position, to Place and to Position and validating the input
        fromPlace = input("\n1. From Cascade \n2. From Cell \n3. From Foundation \nEnter your choice : ")
        check_ip(1, 3, fromPlace)
        if fromPlace == '1':
            fromPos = input("Please enter from Position 1 to 8 : ")
            check_ip(1, 8, fromPos)
            toPlace = input("\n1. To Cascade \n2. To Cell \n3. To Foundation \nEnter your choice : ")
            check_ip(1, 3, toPlace)
        elif fromPlace == '2':
            fromPos = input("Please choose the cell 1 to 4 : ")
            check_ip(1, 4, fromPos)
            toPlace = input("\n1. To Cascade \n2. To Cell \n3. To Foundation \nEnter your choice : ")
            check_ip(1, 3, toPlace)
        else:
            fromPos = input("Please choose the Foundation 1 to 4 : ")
            check_ip(1, 4, fromPos)
            toPlace = input("\n1. To Cascade \n2. To Cell \nEnter your choice : ")
            check_ip(1, 2, toPlace)

        if toPlace == '1':
            toPos = input("Please enter target Cascade 1 to 8 : ")
            check_ip(1, 8, toPos)
        elif toPlace == '2':
            toPos = input("Please enter target Cell 1 to 4 : ")
            check_ip(1, 4, toPos)
        else:
            toPos = input("Please enter target Foundation 1 to 4 : ")
            check_ip(1, 4, toPos)

        # Calling the moveCard function by passing the user input values
        game.moveCard(fromPlace, toPlace, fromPos, toPos)


if __name__ == "__main__":
    main()
