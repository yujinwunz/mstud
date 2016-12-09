import itertools
from cards import *
from evaluate import *

dp = {}
evals = 0

def ev(ncards, suited, cards, bets):
    global dp, evals, payoutcalcs
    if ncards == 5:
        k = (suited, reduce(lambda a, b: a*13+b, cards))
        if k not in dp:
            dp[k] = payout(map(lambda a: Card(a[1]+1, (a[0]%4)*(1-suited)), enumerate(cards)))
        return (dp[k] * bets, None)
    key = (ncards, suited, reduce(lambda a, b: a*13+b, cards), bets)

    if key in dp:
        return dp[key]

    evals += 1
    if evals % 1000 == 0:
        print evals

    best = (0, 0)
    for thisbet in [1, 3]:
        value = 0.0
        for k in range(52):
            if cards.count(k%13) > k/13:
                continue
            if suited and k < 13:
                value += (ev(ncards+1, 1, sorted(cards + [k%13]), bets + thisbet)[0] - thisbet) / (52. - ncards)
            else:
                value += (ev(ncards+1, 0, sorted(cards + [k%13]), bets + thisbet)[0] - thisbet) / (52. - ncards)
        best = max(best, (value, thisbet))
    dp[key] = best

    return best

if __name__=="__main__":
    tot = 0.
    lol = 0
    for i in range(52):
        for j in range(52):
            if i == j:
                continue
            lol += 1
            if i/13 == j/13:
                tot += (ev(2, 1, [i%13, j%13], 1)[0] - 1)
            else:
                tot += (ev(2, 0, [i%13, j%13], 1)[0] - 1)
    print lol / (52. * 51.)
    print "ev of entire game:", tot / lol
    for i in filter(lambda a: len(a)>2, dp.keys()[:100]):
        print i[1], i[3], map(lambda a: i[2]/(13**a)%13 + 1, range(i[0])), dp[i]
    while True:
        ncards = int(raw_input("num cards"))
        cards = map(lambda a: int(raw_input("card %d"%(a,))) - 1, range(ncards))
        suited = int(raw_input("suted? "))
        bets = int(raw_input("bets "))
        print ev(ncards, suited, cards, bets)

def playOptimallyBasic(cards, bets):
    """returns either 0, 1, or 3"""
    ptsTable = [0,2,0,0,0,0,1,1,1,1,1,2,2,2]
    cards = sorted(cards)
    pts = sum([ptsTable[i.rank] for i in cards])
    if len(cards) == 2:
        if hasPair(cards): return 3
        if isStraightFlush(cards) and cards[0].rank >= 5: return 1
        if pts >= 2: return 1
        return 0

    if len(cards) == 3:
        if rankOfPair(cards) == 1 or rankOfPair(cards) >= 6 or hasThreeOfAKind(cards):
            return 3
        if isBroadwayDraw(cards) and isFlush(cards):
            return 3
        if isStraightFlush(cards):
            if cards[1].rank >= 6: return 3
            else: return 1
        if isStraight(cards, 1) and isFlush(cards) and pts >= 4:
            return 3
        if isStraight(cards, 2) and isFlush(cards) and pts >= 5:
            return 3
        if isFlush(cards): return 1
        if hasPair(cards): return 1
        if pts >= 3: return 1
        if isStraight(cards) and cards[0].rank >= 4: return 1
        if isStraight(cards, 1) and pts >= 2: return 1
        return 0

    if len(cards) == 4:
        if rankOfPair(cards) == 1 or rankOfPair(cards) >= 6:
            return 3
        if hasTwoPair(cards) or hasThreeOfAKind(cards) or isFourOfAKind(cards):
            return 3
        if isFlush(cards):
            return 3
        if isStraight(cards) and (cards[1].rank >= 6):
            return 3
        if isStraightDraw(cards):
            return 1
        if hasPair(cards):
            return 1
        if pts >= 4:
            return 1
        if pts >= 3 and bets >= 5:
            return 1
        return 0

def checkOptimality():
    diffs = sames = 0
    for rainbow in [0, 1]:
        for bets in [1, 2, 3, 4, 5, 6, 7]:
            for nshown in range(min(max(2, bets+1), 3), min(5, bets+2)):
                for ranks in itertools.combinations_with_replacement(range(1, 14), nshown):
                    if not rainbow and len(set(ranks)) != len(ranks):
                        continue
                    cards = [Card(a, 0) for a in ranks]
                    cards[0].suit = rainbow
                    if playOptimallyBasic(cards, bets) != ev(nshown, 1 - rainbow, [a-1 for a in ranks], bets)[1]:
                        print "ranks", ranks, "bets", bets, "rainbow?", rainbow, playOptimallyBasic(cards, bets), ev(nshown, 1-rainbow, [a-1 for a in ranks], bets)
                        diffs += 1
                    else:
                        sames += 1
    print diffs, sames



