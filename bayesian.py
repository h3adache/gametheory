import prob as p

def findP(payoffs_a, payoffs_b) :
    "find the payoffs by first finding the strictly dominate strategy, first payoff is p, next is 1-p"
    p.p2(payoffs_a[0], payoffs_b[0], payoffs_a[1], payoffs_b[1])

def payoff(p, a, b) :
    return a * p + b * (1 - p)
