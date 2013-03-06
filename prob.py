def prob() :
    help()
    a,b,c,d = input("enter the payoffs:")
    p(a,b,c,d)

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

def p3(a,b,c,d,e,f,g,h,i) :
    p1,q1,const1 = solveHalf(a,b,c,d,e,f)
    p2,q2,const2 = solveHalf(a,b,c,g,h,i)

def solveHalf(a,b,c,d,e,f) :
    p = a - c - d + f
    q = b - e - c + f
    const = c - f

    print '{}p'.format(p)
    print '{}q'.format(q)
    print '{} const'.format(const)

    return p, q, const

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
