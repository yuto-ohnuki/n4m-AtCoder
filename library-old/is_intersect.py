""" ２本の線分が交差するか否かを返す関数 """
import numpy as np

def is_intersect(a1,a2,b1,b2):
    """ 外積<=0の条件を両方の線分に対して確認 """
    
    # b1,b2が線分Aに対して逆側に位置する条件　： cond1<=0
    cond1 = np.cross(a2-a1, b1-a1) * np.cross(a2-a1, b2-a1)
    
    # a1,a2が線分Bに対して逆側に位置する条件 : cond2<=0
    cond2 = np.cross(b2-b1, a1-b1) * np.cross(b2-b1, a2-b1)
    return cond1<=0 and cond2<=0

# 対称となる線分における端点A, Bのx,y座標
Ax, Ay = map(int,input().split())
Bx, By = map(int,input().split()) 
a1 = np.array([Ax, Ay])
a2 = np.array([Bx, By])

# 交差を調べたい線分の端点のx,y座標
x1,y1,x2,y2 = map(int,input().split())
b1 = np.array([x1, y1])
b2 = np.array([x2, y2])

if is_intersect(a1,a2,b1,b2):
    print('Cross')
else:
    print('Not Cross')