import random

class Card(object):
    def __init__(self, rank, suit=None):
        if suit == None:
            self.rank = rank % 13 + 1
            self.suit = rank / 13
        else:
            self.rank = rank
            self.suit = suit
    ACE = 1
    KING = 13
    QUEEN = 12
    JACK = 11
    rank_map = ["Ace", "Deuce", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit_map = ["Diamond", "Club", "Heart", "Spade"]
    def __str__(self):
        return "%s of %ss" % (Card.rank_map[self.rank-1], Card.suit_map[self.suit])

class Deck(object):
    def __init__(self, decks=1, shuffled=True):
        self.cards = map(lambda a: Card(a), range(52)) * decks
        if shuffled:
            random.shuffle(self.cards)
    def peek(self):
        return self.cards[0]
    def deal(self):
        return self.cards.pop(0)
    def shuffle(self):
        random.shuffle(self.cards)
    def __str__(self):
        return str(self.cards)
