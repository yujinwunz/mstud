from cards import *
from evaluate import *
from player import *

def isSuited(cards):
    for i in range(1, len(cards)):
        if cards[0].suit != cards[i].suit:
            return False
    return True

if __name__ == "__main__":
    antesPaid = 0
    betsPaid = 0
    won = 0
    payouts = {}
    for i in range(500000):
        antesPaid += 1
        bets = 1
        cards = []
        deck = Deck()
        for j in range(5):
            if j >= 2:
                thisbet = ev(j, isSuited(cards), [k.rank - 1 for k in cards], bets)[1]
                if thisbet == 0:
                    continue
                bets += thisbet
            cards.append(deck.deal())
        winnings = payout(cards)
        payouts[winnings] = payouts.get(winnings, 0) + 1
        won += winnings * bets
        betsPaid += bets

        if antesPaid % 10000 == 0:
            print "antes paid:", antesPaid
            print "bets paid:", betsPaid
            print "won:", won
            print "diff:", won - betsPaid
            print "diff %:", float(won - betsPaid) * 100 / betsPaid
            print "edge %:", float(won - betsPaid) * 100 / antesPaid
            print payouts
            print
