from deck import Deck, Card

class PokerHand:
    """
    A class to represent a 5-card poker hand drawn from a deck.

    Attributes:
    -----------
    _cards : list of Card
        The list of 5 cards dealt to the hand.
    """

    def __init__(self, deck):
        """
        Deal 5 cards from the given deck to form a poker hand.

        Parameters:
        -----------
        deck : Deck
            The deck from which to draw cards.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Get the list of cards in the hand.

        Returns:
        --------
        list of Card
        """
        return self._cards

    def __str__(self):
        """
        Return a string representation of the poker hand.

        Returns:
        --------
        str
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Check if the hand is a flush (all cards have the same suit).

        Returns:
        --------
        bool
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Check if the hand is a full house (3 of one rank and 2 of another).

        Returns:
        --------
        bool
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Compute a score representing how many card ranks match in the hand.

        - Pair: 2 matches
        - Two Pair: 4 matches
        - Trips: 6 matches
        - Full House: 8 matches
        - Quads: 12 matches

        Returns:
        --------
        int
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if the hand is a single pair.

        Returns:
        --------
        bool
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Check if the hand is two pairs.

        Returns:
        --------
        bool
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Check if the hand is three of a kind.

        Returns:
        --------
        bool
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Check if the hand is four of a kind.

        Returns:
        --------
        bool
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Check if the hand is a straight (5 consecutive ranks with no repeats).

        Returns:
        --------
        bool
        """
        # Sort the cards by rank index
        self.cards.sort(key=lambda card: Card.RANKS.index(card.rank))
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4


# --- Simulation: estimate probability of a straight ---

count = 0      # total number of hands simulated
matches = 0    # number of straights observed

while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
        print(hand)
    count += 1

print(f"probability of a straight is {100 * matches / count}%")


