import numpy as np

""" 点ｚが中心c半径rの円の内部にあるかを判定 (0:円周上、-1:円内、1:円外) """
def c_inCircle(z, c, r, epsilon=1e-6):
    d = abs(z-c)
    if abs(r-d) < epsilon:
        return 0
    elif r-d>0:
        return -1
    return 1

""" 2点(x1,y1),(x2,y2) [x1!=x2]を通る直線の方程式 """
def linear_func(x,x1,y1,x2,y2):
    return ((y2-y1)/(x2-x1))*(x-x1) + y1

""" 点と線分の距離 ( 線分A(x1,y1),B(x2,x2)からC(x3,y3)への距離 ) 
def distance(func, x,y):
    u = np.array([x2-x1, y2-y1])
    v = np.array([x3-x1, y3-y1])
    return abs(np.cross(u,v) / np.linalg.norm(u))"""

""" 3点(x1,y1),(x2,y2),(x3,y3)を頂点とする三角形の面積 """
def triangle_size(x1,x2,x3,y1,y2,y3):
  return abs((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3))/2