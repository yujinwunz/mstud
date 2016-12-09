from cards import *
from evaluate import *

def genhand():
    d = Deck()
    return [d.deal() for i in range(5)]

if __name__ == "__main__":
    score = 0.
    for i in range(100000):
        score += payout(genhand())
    print "in 100000 hands, we won", score
