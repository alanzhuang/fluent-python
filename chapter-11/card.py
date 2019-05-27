from random import shuffle
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


def set_card(self, position, card):
    self._cards[position] = card

FrenchDeck.__setitem__ = set_card
deck = FrenchDeck()
shuffle(deck)
print(deck[:5])
