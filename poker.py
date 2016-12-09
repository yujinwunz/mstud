from cards import *
import random

def isStraight(cards, gaps=0):
    cards = sorted(cards)
    for i in range(1, len(cards)):
        if cards[i].rank == cards[i-1].rank:
            return False
    return cards[0].rank + len(cards)-1 + gaps == cards[-1].rank

def isOneGapper(cards):
    return isStraight(cards, 1)

def isTwoGapper(cards):
    return isStraight(cards, 2)

def isStraightDraw(cards):
    if len(cards) >= 5:
        return False
    return isStraight(cards, 0) or isStraight(cards, 1) or isStraight(cards, 2)

def isFlush(cards):
    for i in range(1, len(cards)):
        if cards[i].suit != cards[i-1].suit:
            return False
    return True

def isStraightFlush(cards):
    return isStraight(cards) and isFlush(cards)

def isStraightFlushDraw(cards):
    return isStraightDraw(cards) and isFlush(cards)

def hasPair(cards):
    cards = sorted(cards)
    for i in range(1, len(cards)):
        if cards[i].rank == cards[i-1].rank:
            return True
    return False

def rankOfPair(cards):
    rankMap = [0] * 13
    for i in cards:
        rankMap[i.rank-1] += 1
    if rankMap[0] >= 2:
        return 1
    for i in range(12, 0, -1):
        if rankMap[i] >= 2:
            return i+1
    return None

def hasTrips(cards):
    cards = sorted(cards)
    for i in range(2, len(cards)):
        if cards[i].rank == cards[i-1].rank == cards[i-2].rank:
            return True
    return False

def isFullHouse(cards):
    cards = sorted(cards)
    if len(cards) != 5:
        return False
    if cards[0].rank != cards[1].rank or cards[3].rank != cards[4].rank:
        return False
    if cards[2].rank != cards[0].rank and cards[2].rank != cards[4].rank:
        return False
    return True

def isFourOfAKind(cards):
    cards = sorted(cards)
    return cards[1].rank == cards[4].rank or cards[0].rank == cards[3].rank

def hasTwoPair(cards):
    """returns true for trips"""
    cards = sorted(cards)
    if cards[1].rank == cards[0].rank or cards[1].rank == cards[2].rank:
        if cards[3].rank == cards[2].rank or cards[3].rank == cards[4].rank:
            return True
    return False




