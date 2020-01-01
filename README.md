# Highest-Card-Draw
A command line python game that deals a deck of cards supplied by the user and determines which round is won by which player

### Included Files
* deck.py
* README

### Description: 
* deck.py has one function, readFile() which reads in file from command line and puts its content into a list format, each element containing a two character strength representing a card. Returns: The newly createdDeck

* deck.py has one class named Deck which further contains 3 methods aside from __init__ and __str__: 
		* deal(): Deals one card from top of deck. 
        Returns: Either the top card (first element in the deck list), or False if there are no cards left in the deck

* validate(): Checks whether the deck is a valid 52 card deck or not.
			Returns:
			   (is_valid, msg): a tuple containing a Boolean value indicating whether
								the deck is valid (True) or not (False), and a string
								that is either empty (when deck is valid) or contains
								information about why the deck is no valid

* highDraw(): Plays the "High Draw" game where card is dealt to the player and dealer respectively and alternatively till deck is empty. Results are directly printed to the screen with each round.
		Returns: Nothing


### Running instructions: 
* When running the program, call it along with the input file that needs to be read. For eg: >> python3 deck.py example1 - where example1 is the input file.

### Assumptions: 
* File called in command line exists.
* File called in command line has a series of two character strings in every line. These strings may be upper/lower case and may contain whitespaces around them (but not in between)
* File may have invalid cards.

