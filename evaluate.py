from cards import *
import random

def isBroadway(cards):
    cards = sorted(cards)
    if cards[0].rank != 1:
        return False
    for i in range(1, len(cards)):
        if cards[i].rank != 13 - len(cards) + i + 1:
            return False
    return True

def isStraight(cards, gaps=0):
    if isBroadway(cards):
        return True
    cards = sorted(cards)
    for i in range(1, len(cards)):
        if cards[i].rank == cards[i-1].rank:
            return False
    return cards[0].rank + len(cards)-1 + gaps == cards[-1].rank

def isBroadwayDraw(cards):
    for i in cards:
        if i.rank < 10 and i.rank != 1: return False
    return True

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
    for i in range(12, -1, -1):
        if rankMap[i] >= 2:
            return i+1
    return None

def hasThreeOfAKind(cards):
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
    if len(cards) < 4: return False
    if len(cards) == 4:
        return cards[0].rank == cards[-1].rank
    return cards[1].rank == cards[4].rank or cards[0].rank == cards[3].rank

def hasTwoPair(cards):
    """undefined for trips and true for quads"""
    cards = sorted(cards)
    if len(cards) < 4: return False
    if len(cards) == 4:
        return cards[0].rank == cards[1].rank and cards[2].rank == cards[3].rank
    if cards[1].rank == cards[0].rank or cards[1].rank == cards[2].rank:
        if cards[3].rank == cards[2].rank or cards[3].rank == cards[4].rank:
            return True
    return False

def isRoyalFlush(cards):
    if isFlush(cards) and isBroadway(cards):
        return True
    return False

def payout(cards):
    if len(cards) < 5:
        return 0
    if isRoyalFlush(cards):
        return 501
    if isStraightFlush(cards):
        return 101
    if isFourOfAKind(cards):
        return 41
    if isFullHouse(cards):
        return 11
    if isFlush(cards):
        return 7
    if isStraight(cards):
        return 5
    if hasThreeOfAKind(cards):
        return 4
    if hasTwoPair(cards):
        return 3
    if rankOfPair(cards) >= 11 or rankOfPair(cards) == 1:
        return 2
    if rankOfPair(cards) >= 6:
        return 1
    return 0

