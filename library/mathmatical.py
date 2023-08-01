""" 最大公約数 """
def gcd(a,b):
    import math
    return math.gcd(a,b)

""" 最小公倍数 """
def lcm(a,b):
    import math
    x = math.gcd(a,b)
    return a*b//x

""" 約数の列挙 """
def divisor(x):
    ret = []
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            ret.append(i)
            if not i**2 == x:
                ret.append(x//i)

    # ret.sort()
    return ret

""" 素因数分解 """
def prime_decomposition(x):
    ret = []
    i = 2
    while i**2 <= x:
        while x%i == 0:
            ret.append(i)
            x = x // i
        i += 1
    if x > 1:
        ret.append(x)
    
    # ret.sort()
    return ret