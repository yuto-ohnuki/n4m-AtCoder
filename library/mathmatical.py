""" 最大公約数 """
def gcd(a,b):
    import math
    return math.gcd(a,b)

""" 最小公倍数 """
def lcm(a,b):
    import math
    x = math.gcd(a,b)
    return a*b//x

""" 約数列挙 """
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

""" Decimal による除算 """
""" Decimal は PyPy は遅いので注意 """
def decimal_divide(a:str, b:str):
    from decimal import Decimal, getcontext
    getcontext().prec = 100

    assert type(a)==str, "type error"
    assert type(b)==str, "type error"

    a = Decimal(a)
    b = Decimal(b)
    return a/b