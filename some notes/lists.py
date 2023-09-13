def divisors(n):
    return [1] + [x for x in range(2,n) if n % x == 0]
def rational(n,d):
    g = gdc(n,d)
    return [n//g,d//g]
{x:x*x for x in range(10)}