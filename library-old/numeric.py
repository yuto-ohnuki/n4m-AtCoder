"""最大公約数"""
def gcd(a,b):
    import math
    return math.gcd(a,b)

"""最小公倍数"""
def lcm(a,b):
    import math
    f = math.gcd(a,b)
    return a*b//f

"""約数列挙"""
def divisor(n):
    tank = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            tank.append(i)
            if i!=n//i:
                tank.append(n//i)
    tank.sort()
    return tank

"""素因数分解"""
def prime_decomposition(n):
    i = 2
    tank = []
    while i * i <= n:
        while n%i == 0:
            n /= i
            tank.append(i)
        i += 1
    if n > 1:
        tank.append(int(n))
    return tank

"""多数に対する素因数分解 -osa_k法- O(AloglogA+NlogA), A=max{A_i}"""
def osa_k(lst):
    n = 10**6 + 10
    l = [i for i in range(n+1)]
    p=2
    while p*p <= n:
        if l[p] == p:
            for q in range(2*p, n+1, p):
                if l[q] == q:
                    l[q] = p
        p += 1
    ret = []
    for a in lst:
        tmp = set()
        while a > 1:
            tmp.add(l[a])
            a //= l[a]
        ret.append(tmp)
    return ret

"""素数判定"""
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return n!=1

"""エラトステネスの篩 O(Nlog(N)) """
def sieve(n):
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        else:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


"""フィボナッチ数列"""
def fibonacci(n):
    F = [1,1]
    for i in range(1, n-1):
        F.append(F[i] + F[i-1])
    return F

""" 階乗 """
def factorial(x):
    import math
    return math.factorial(x)


"""nCk (逆元ver) """
# combination.pyの方が圧倒的に高速
def comb(n,k):
    nCk = 1
    mod = 10**9+7
    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= mod
    for i in range(1, k+1):
        nCk *= pow(i, mod-2, mod)
        nCk %= mod
    return nCk

""" nHk (重複組み合わせ) """
# n種類のものから重複を許してk個選ぶ場合の数
def overlapping_comb(n,k):
    return comb(n+k-1, k)

""" 逆元 (a^-1 [mod b])"""
# mod_bにおけるaの逆元
# aとbは互いに素
# python3.8以降では pow(a, -1, b)でも獲得可能
def modinv(a, b):
    p = b
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    x %= p
    if x < 0:
        x += p
    return x
