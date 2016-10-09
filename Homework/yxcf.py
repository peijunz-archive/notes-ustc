#!/usr/bin/env python3
from math import *
#请用python3运行本程序

def sid(x,y):
    '''在边界(side)上的函数'''
    p=(x,y)
    if p==(0,0) or p==(0,1) or p==(1,0) or p==(1,1):
        return 1/2
    if abs(x)<1e-5 or abs(x-1)<1e-5:
        return 1
    elif abs(y)<1e-5 or abs(y-1)<1e-5:
        return 0
    else:
        return 1/2

def yxcf(f,n,rep=100):
    '''超松驰迭代

    f   边值函数
    n   单一维度上划分的格数
    rep 迭代次数，默认100次'''
    phi=[[0 for i in range(0,n+1)] for i in range(0,n+1)]
    omega=2/(1+sin(pi/n))
    s=[]
    for i in range(1,n):
        s.append((0,i))
        s.append((n,i))
        s.append((i,0))
        s.append((i,n))
    s=s+[(0,0),(0,n),(n,0),(n,n)]
    for i in s:
        x=i[0]
        y=i[1]
        phi[x][y]=f(x/n,y/n)
    for t in range(0,rep):
        for i in range(1,n):
            for j in range(1,n):
                t=(phi[i-1][j]+phi[i+1][j]+phi[i][j+1]+phi[i][j-1])/4
                phi[i][j]=phi[i][j]+omega*(t-phi[i][j])
    return phi

def print3(p):
    '''保留三位小数输出二维数组'''
    for i in p:
        for j in i:
            print("%5.3f\t"%(j),end='')
        print('')

def gridcf(n,re=100):
    '''做有限差分迭代，返回phi'''
    return yxcf(sid,n,re)

if __name__ == "__main__":
    p=gridcf(15)
    print3(p)
