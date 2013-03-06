def prob() :
    help()
    a,b,c,d = input("enter the payoffs:")
    p(a,b,c,d)

def help() :
    print 'use p(a, b, c, d)\n'

def p(a, b, c, d):
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

    print '{}p'.format(p)
    print '{}q'.format(q)
    print '{} const'.format(const)

    return p, q, const

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
