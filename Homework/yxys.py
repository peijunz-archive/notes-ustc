#!/usr/bin/env python3
from scipy import *
from scipy.sparse import *
#由于调用了scipy中的稀疏矩阵类型，因此依赖于scipy库，请安装python3-scipy后用python3运行
from yxcf import sid,print3
#从上一个有限差分导入边值函数以及保留三位有效数字输出
def tricot(a,b,c):
    '''计算三角形的cot(A,B,C)

    a,b,c   三个点的坐标'''
    [a,b,c]=array([a,b,c])  #将三个点的数据类型转换为array数列
    #s为三角形面积的两倍，下面计算面积
    s = abs((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))
    #计算三条首尾相连的边矢量
    va = b-c
    vb = c-a
    vc = a-b
    #计算三个角的cot值
    cota = -dot(vb, vc)/s
    cotb = -dot(vc, va)/s
    cotc = -dot(va, vb)/s
    return array([cota, cotb, cotc])

def tris(n):
    '''产生所有三角形对应的三点组(P_1,P_2,P_3)，其中P_i=(x_i,y_i)

    n   单个维度的格数'''
    h=1/n
    tri=[]
    for i in range(n):
        for j in range(n):
            tri.append([ (i*h, j*h), ((i+1)*h, j*h), ((i+1)*h, (j+1)*h) ])
            tri.append([ (i*h, j*h), (i*h, (j+1)*h), ((i+1)*h, (j+1)*h) ])
    return tri

def points(n):
    '''产生顶点组，不包括边值点

    n   单个维度的格数'''
    h=1/n
    poi=[]
    for i in range(1,n):
        for j in range(1,n):
            poi.append((i*h,j*h))
    return poi

def sdp(n):
    '''产生边界上的顶点side points

    n   单个维度的格数'''
    s=[]
    h=1/n
    #边界上的点
    for i in range(1,n):
        s.append((0,i*h))
        s.append((n*h,i*h))
        s.append((i*h,0))
        s.append((i*h,n*h))
    #加上四个顶点
    s=s+[(0,0),(0,1),(1,0),(1,1)]
    return s

def yxys(poi,pos,tri,side,rep=50,omega=1.6):
    '''给定点列、三角形与边值，用有限元素法解Laplace第一边值问题，迭代次数rep和松弛因子omega可选

    poi     内点
    pos     边界点
    tri     三角形组
    side    边值函数
    rep     迭代次数
    omega   松弛迭代因子'''
    m=len(poi)
    l=len(pos)
    phi=zeros(m+l)
    #构造由点到序数的映射词典d
    d={}
    for i in range(m):
        d[poi[i]]=i
    for i in range(l):
        d[pos[i]]=i+m
        phi[i+m]=side(*pos[i])
    K=dok_matrix((m, m+l))          #非对角元矩阵
    kd=zeros(m)                     #对角元矩阵
    for t in tri:
    #对每个三角形计算出相应权值
        kk=tricot(*(t))
        for i in range(3):
        #对三个顶点循环
            j=(i+1)%3
            k=(i+2)%3
            #定义ni,nj,nk简化代码输入
            [ni,nj,nk]=[d[t[i]],d[t[j]],d[t[k]]]
            if ni<m:
            #判断是内点后加上相应权重
                kd[ni]+=kk[j]+kk[k]
                K[ni,nj]+=kk[k]
                K[ni,nk]+=kk[j]
    K=K.tocsr()
    for num in range(rep):
    #开始迭代
        for i in range(m):
            s=K[i].dot(phi)
#            key=[w[1] for w in K[i].keys()]
#            for j in key:
#                s+=phi[j]*K[i,j]
            t=s/kd[i]
            phi[i]=phi[i]+omega*(t-phi[i])
    return phi

def gridtri(n,re=50):
    '''做网格+斜线划分并返回phi值数列,迭代次数可选

    n   某个维度的划分格数。
    re  迭代次数，是可选参数'''
    pos=sdp(n)
    poi=points(n)
    tri=tris(n)
    ph=yxys(poi,pos,tri,sid,rep=re)
    p=array(poi+pos)*n
    phi=zeros((n+1,n+1))
    for i in range(len(p)):
        (x,y)=p[i]
        phi[x,y]=ph[i]
    return phi

if __name__=='__main__':
    n=10
    p=gridtri(n)
    print3(p)
