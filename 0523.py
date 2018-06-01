#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def ik((x,y),(L1,L2),(ang1,ang2),a,b):
    ang=np.array([[ang1],[ang2]])
    i=1
    while True :
        px=a-float(x)
        py=b-float(y)
        if px<1 and px>-1 and py<1 and py>-1 :
            print '理想値x=',a,'y=',b
            fig.show()
            break
        J1=L1*cos(ang1)+L2*cos(ang1+ang2)
        J2=L2*cos(ang1+ang2)
        J3=-L1*sin(ang1)+L2*sin(ang1+ang2)
        J4=-L2*sin(ang1+ang2)
        J=np.array([[J1,J2],[J3,J4]])

        inJ=np.linalg.inv(J)

        dX = np.array([[px/10],[py/10]])
        dang=np.dot(inJ,dX)
        ang=ang+dang
        x=L1*sin(ang[0])+L2*sin(ang[0]+ang[1])
        y=L1*cos(ang[0])+L2*cos(ang[0]+ang[1])
        angle1=ang[0]*180/pi
        angle2=ang[1]*180/pi
        fig = plt.figure()

        ax = fig.add_subplot(1,1,1)

        ax.scatter(x,y)


        print i, 'px=',px,'py=',py,'θ1=',angle1,'θ2=',angle2,'x=',x,'y=',y
        i+=1

    return ang1, ang2

def fk((L1,L2),(ang1,ang2)):
    x=L1*sin(ang1)+L2*sin(ang1+ang2)
    y=L1*cos(ang1)+L2*cos(ang1+ang2)
    return x,y

def main():
    #初期状態
    L=(200,200)  #リンクの長さ(mm)
    ang = (90*(math.pi)/180, -90*(math.pi)/180) #初期の角度
    X=fk(L,ang)                                 #初期の位置（順運動学呼び出し)
    print X


    #目的地選択
    print "どの位置に手先を持って行きたいですか？\nx座標"
    a=input()
    print "y座標"
    b=input()
    x=float(a)#-X[0]                             #目的地までの差を計算
    y=float(b)#-X[1]                             #目的地までの差を計算
    #出力・計算
    ang=ik(X,L,ang,x,y)
    fig.show()


if __name__ == '__main__':
    main()
