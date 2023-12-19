import string

""" 大文字・小文字の一覧 """
lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
full_chars = string.ascii_letters
digits = string.digits

""" 文字　→　idxへ """
def to_idx(c):
    return ord(c) - ord('a')

""" idx →　文字へ"""
def to_char(idx):
    return chr(idx + ord('a'))

""" k進数 → 10進数 """
def base_10(num, k):
  ret = 0
  for s in str(num):
    ret *= k
    ret += int(s)
  return ret

""" 10進数 → k進数 """
def base_k(num, k):
  ret = ''
  while num:
    if num%k>=10:
      return -1
    ret += str(num%k)
    num //= 10
  return int(ret[::-1])

""" 文字列からindexの獲得 """
def get_index(s):
    set_s = set(s)
    dct = {}
    for char in set_s:
        dct[char] = []
    for idx, char in enumerate(s):
        dct[char] += [idx]
    return dct

""" indexの文字を変更 """
def replace_from_idx(s, l_idx, c):
    return s[:l_idx]+c+s[l_idx+len(c):]

""" ランレングス圧縮 """
def rle_comp(lst):
  from itertools import groupby
  return [[key,len(list(group))] for key,group in groupby(lst)]

""" 文字変換 """
def convert_str_from_dict(s, dic):
  tbl = str.maketrans(dic)
  return s.translate(tbl)