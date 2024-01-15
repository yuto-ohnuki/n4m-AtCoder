import itertools

""""リストを最初から数えて、同じ値のものを区切って出力する"""
def group_count(bi = [0,0,0,1,1,0,0,0,1,1,0,1]):
    gr = itertools.groupby(bi)
    #groupはイテレータ
    for key, group in gr:
        print(key, list(group))

"""全ての順列組み合わせ"""
def f1(lst=[1,2,3]):
    return list(itertools.permutations(lst))
#print(f1())

"""全ての組み合わせ"""
def f2(lst=[1,2,3], n=2):
    return list(itertools.combinations(lst, n))
#print(f2())

""" 直積 """
# Aから１つ、Bから１つの要素をとった場合の総組み合わせを返す
#   ⇒ for文のネストを減らす
def f3(A=[1,2,3], B=[4,5]):
    return list(itertools.product(A, B))
#print(f3())

""" 重複順列 (repeat個のAの直積を返す) """
def f4(A=[1,2,3], repeat=3):
    return list(itertools.product(A, repeat=repeat))
#print(f4())


""" 重複組み合わせ """
def f5(A=[1,2,3], r=3):
    return list(itertools.combinations_with_replacement(A, r))
print(f5())


"""リストから複数個のインデックスを返す  (tgの値を持つidxの列挙)"""
def f6(lst=[1,2,3,2,3,2,1], tg=2):
    idx_num = [e for e, v in enumerate(lst) if v == tg]
    return idx_num
#print(f6())
