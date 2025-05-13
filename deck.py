import random

class Card:
    """
    A class representing a single playing card with a rank and suit.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, suit, rank):
        """
        Initialize a Card object with validation.

        Parameters:
        -----------
        suit : str
            One of the four suit symbols.
        rank : str
            One of the standard card ranks (2–10, J, Q, K, A).
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Compare equality based on rank.
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compare cards based on rank order.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        User-friendly string representation (e.g., 'A♠').
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Debug-friendly representation.
        """
        return self.__str__()

    @property
    def suit(self):
        """Getter for suit."""
        return self._suit

    @property
    def rank(self):
        """Getter for rank."""
        return self._rank


class Deck:
    """
    A class representing a standard 52-card deck.
    """

    def __init__(self):
        """
        Initialize a full deck of 52 cards.
        """
        self._deck = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def __str__(self):
        """
        Return a concise string showing all cards in the deck.
        """
        return ", ".join(str(card) for card in self._deck)

    def shuffle(self):
        """
        Shuffle the deck randomly.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deal (remove and return) the top card of the deck.

        Returns:
        --------
        Card
            The card removed from the top of the deck.
        """
        if not self._deck:
            raise IndexError("No cards left in the deck")
        return self._deck.pop(0)


# --- Example usage ---

if __name__ == "__main__":
    deck = Deck()
    print("Initial deck:")
    print(deck)

    deck.shuffle()
    print("\nShuffled deck:")
    print(deck)

    print("\nDealing a card:")
    print(deck.deal())
