
n = int(input())

# 10進数 -> 2進数
bit_n = format(n, 'b')
print(bit_n)

# 10進数 -> 2進数 (0-padding)
bit_n = format(n, '0{}b'.format(10))
print(bit_n)

# 2進数 -> 10進数
n_ = int(bit_n, 2)
print(n_)

# bit全探索
n = 6
lst = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(2**n):
    tmp = []
    for j in range(n):
        if ((i >> j) & 1):      # 順に右にシフトして最下位bitのフラグを確認
            tmp.append(lst[j])
    print(tmp)
