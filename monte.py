from cards import *
from evaluate import *
from player import *
from marked import *

def isSuited(cards):
    for i in range(1, len(cards)):
        if cards[0].suit != cards[i].suit:
            return False
    return True

lastDiff = 0

if __name__ == "__main__":
    antesPaid = 0
    betsPaid = 0
    won = 0
    payouts = {}

    busts = 0
    hits = 0
    stack = 50

    for i in range(500000):
        antesPaid += 1
        bets = 1
        cards = []
        deck = Deck()
        njacks = (deck.cards[2].rank == 11) + (deck.cards[3].rank == 11) + (deck.cards[4].rank == 11)
        jackMap = tuple(map(lambda a: 2 if a.rank == 12 else (1 if a.rank == 11 else 0), deck.cards))
        for j in range(5):
            if j >= 2:
                thisbet = markedJackDp(len(cards), isFlush(cards), map(lambda a: a.rank-1, cards), bets, jackMap)[1]
                if thisbet == 0:
                    continue
                bets += thisbet
            cards.append(deck.deal())
        winnings = payout(cards)
        payouts[winnings] = payouts.get(winnings, 0) + 1
        won += winnings * bets
        betsPaid += bets

        stack -= bets
        stack += winnings * bets
        if stack <= 0:
            busts += (stack - 50) / -200.0
            stack = 50
        if stack > 100:
            hits += (stack - 50) / 200.0
            stack = 50

        if antesPaid % 50 == 0:
            print "in the last 50 hands diff:", won - betsPaid - lastDiff
            lastDiff = won - betsPaid
            print "busts: %f hits: %f" % (busts, hits)
            print "antes paid:", antesPaid
            print "bets paid:", betsPaid
            print "won:", won
            print "diff:", won - betsPaid
            print "diff %:", float(won - betsPaid) * 100 / betsPaid
            print "edge %:", float(won - betsPaid) * 100 / antesPaid
            print payouts
            print
