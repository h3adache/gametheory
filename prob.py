import math

def prob() :
    payoffs = input("enter the payoffs:")
    methods = {'p2' : p2, 'p3' : p3}
    size = math.sqrt(len(payoffs))

    assert size == 2 or size == 3, "Can't handle size %s problems" % size

    methods['p%s' % int(size)](*payoffs)

def p2(a, b, c, d):
    e = a - c
    f = d - b
    g = f + e
    gfcd = gcd(f, g)

    print 'p = {} / {}'.format(f/gfcd, g/gfcd)

def p3(a,b,c,d,e,f,g,h,i) :
    p1,q1,c1 = solveHalf(a,b,c,d,e,f)
    p2,q2,c2 = solveHalf(a,b,c,g,h,i)

    xp = -c1 * q2 + c2 * q1
    yp = -p2 * q1 + p1 * q2

    xq = -c1 * yp - p1 * xp
    yq = q1 * yp

    xr = yp * yq - xp * yq - xq * yp
    yr = yp * yq

    prettyPrint('p', xp, yp)
    prettyPrint('q', xq, yq)
    prettyPrint('r', xr, yr)

def prettyPrint(v, vc, vp) :
    pgcd = gcd(vc, vp)
    x = vc / pgcd
    y = vp / pgcd

    print '{} = {} / {}'.format(v, x, y)

def solveHalf(a,b,c,d,e,f) :
    p = a - c - d + f
    q = b - e - c + f
    const = c - f

    return p, q, const

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
