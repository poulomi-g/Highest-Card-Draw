#-----------------------------------------------------
# Name: Poulomi Ganguly
# ID: 1598887
# CMPUT 274, Fall 2019
# 
# Weekly Exercise 4: High Draw Game
#-----------------------------------------------------

import sys
import copy


class Deck:
	"""
	Stores playing cards
	"""
	
	def __init__(self, cards):
		'''Initializes attribute for deck of cards
		
		Arguments:
			cards: list of two-character strings representing cards
		'''
		self.__deck = copy.deepcopy(cards)
		
	def deal(self):
		'''Deals one card from top of deck.
		
		Returns:
			Either the top card (first element in the deck list), or
			False if there are no cards left in the deck
		'''        
		if len(self.__deck) > 0:
			topCard = self.__deck[0]
			del self.__deck[0]
			return topCard
		else:
			return False


	
	def validate(self):
		'''Checks whether the deck is a valid 52 card deck or not.
		
		Returns:
		   (is_valid, msg): a tuple containing a Boolean value indicating whether
							the deck is valid (True) or not (False), and a string
							that is either empty (when deck is valid) or contains
							information about why the deck is no valid
		'''         
		rankList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T","J", "K", "Q"]
		SuitList = ["C", "S", "D", "H"]

		# Checking if every card is a two letter string:


		j = 0
		counter = 0

		while j < len(self.__deck):
			if (self.__deck[j][0] not in rankList) or (self.__deck[j][1] not in SuitList):
				return (False, "Card {} is not a valid card".format(self.__deck[j]))
			j += 1

		if len(self.__deck) < 52:
			return (False, "Incomplete deck.")

		uniqueDeck = set(self.__deck)

		if len(uniqueDeck) != len(self.__deck):
			return (False, "Deck contains duplicate cards")

		return (True, "")   
	
	def highDraw(self):

		'''Plays the "High Draw" game where card is dealt to the player and dealer respectively and alternatively till deck is empty.
		Results are directly printed to the screen with each round.

		
		Returns: Nothing
		'''

		# A list that contains the heirarchy of cards in defined order.
		cardRanking = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

		# Deck in input file is validated
		if self.validate()[0] == False:
			print(self.validate()[1])
			exit()

		else:
			i = 0
			flag = 0

			# While loops only continues as long as self.deal() returns a card value and not false.
			while flag == 0:

				opponentCard = self.deal()
				dealerCard = self.deal()

				i += 1

				if opponentCard != False:

					# Index of card rank in cardRanking is found and ranks are compared.
					dealerRank = cardRanking.index(dealerCard[0])
					opponentRank = cardRanking.index(opponentCard[0])

					if dealerRank == opponentRank:
						print("Round {}: Tie!".format(i))
					elif dealerRank > opponentRank:
						print("Round {}: Dealer wins!".format(i))
					else:
						print("Round {}: Player wins!".format(i))
				else:
					flag = 1


	def __str__(self):
		'''Creates custom string to represent deck object
		
		Returns:
		   String representation of deck object
		'''         
		return "-".join(self.__deck)


def readFile(fileName):

	'''Reads file and creates an object containing list of cards
		
	Returns:
		  The newly made deck containing the list of Upper case cards, createdDeck
	'''    
	with open(fileName,"r") as fin:
		fileList = fin.read()

	createdDeck = Deck((fileList.upper()).split())

	return createdDeck

if __name__ == "__main__":

	deck1 = readFile(sys.argv[1])

	deck1.highDraw()

