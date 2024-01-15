# 右に90度回転
def right_rotation(mat):
  """
  1.転置
  2.上下反転
  """
  ret = []
  for x in zip(*mat[::-1]):
    ret.append(''.join(x))
  return ret

# 左に90度回転
def left_rotation(mat):
  """
  1.上下反転
  2.転置
  """
  ret = []
  mat_s = list(zip(*mat))
  for x in mat_s[::-1]:
    ret.append(''.join(x))
  return ret