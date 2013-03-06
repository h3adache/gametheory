def prob() :
    help()
    a b c d = input("enter the payoffs:")


def help() :
    print 'use p(a, b, c, d)\n'
    print 'where, in a 2 player game(x,y):\n'
    print 'a := payoff for x for w1 if y plays w1\n'
    print 'b := payoff for x for w1 if y plays w2\n'
    print 'c := payoff for x for w2 if y plays w1\n'
    print 'd := payoff for x for w2 if y plays w2\n'

def p(a, b, c, d):
    e = a - c
    f = d - b
    g = f + e
    gfcd = gcd(f, g)

    print 'p = {} / {}'.format(f/gfcd, g/gfcd)

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
